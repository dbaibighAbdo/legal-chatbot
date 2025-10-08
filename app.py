import json
import re
from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Charger le fichier JSON contenant les articles de loi
def load_laws():
    with open('legal_db.json', 'r', encoding='utf-8') as file:
        return json.load(file)

laws_data = load_laws()

openai.api_key = os.getenv("API_KEY")

# Fonction pour normaliser le texte (enlever les accents, majuscules, etc.)
def normalize(text):
    return re.sub(r"[^\w\s]", "", text.lower())

def generate_legal_response(query):
    """Génère une réponse juridique basée sur la base locale et OpenAI si nécessaire."""
    try:
        normalized_query = normalize(query)
        article_number = None

        # Trouver un numéro d'article dans la question
        match = re.search(r"article\s+(\d+)", normalized_query)
        if match:
            article_number = int(match.group(1))

        matched_article = None

        if article_number:
            # Chercher un article correspondant au numéro ET à la loi mentionnée dans la requête
            for law in laws_data:
                if law['article_number'] == article_number and normalize(law['law']) in normalized_query:
                    matched_article = law
                    break

        if matched_article:
            response = f"Article {matched_article['article_number']} du {matched_article['law']} :\n{matched_article['text']}"
            return response

        # Sinon, on utilise OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """Tu es un expert en droit marocain spécialisé dans la constitution et les lois fondamentales. 
                Tes réponses doivent être:
                - Précises et basées sur les textes de loi marocains
                - En français professionnel
                - Structurées et claires
                - Avec des références aux articles de loi quand possible
                - Avec une mention que ce n'est pas un conseil juridique"""},
                {"role": "user", "content": query}
            ],
            temperature=0.3,
            max_tokens=500
        )

        chat_response = response.choices[0].message['content'].strip()

        return chat_response

    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Désolé, je rencontre une difficulté technique. Veuillez reformuler votre question."


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    query = request.form['question']
    response = generate_legal_response(query)
    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True)
