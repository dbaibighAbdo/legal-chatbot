# ⚖️ Chatbot Juridique Marocain

Un **assistant juridique intelligent** spécialisé dans le **droit marocain**, capable de répondre automatiquement à des questions légales en **français**.  
Ce projet combine **intelligence artificielle**, **traitement du langage naturel (NLP)** et **technologies web modernes** pour offrir une assistance juridique rapide, claire et fiable.

---

## 🧠 Objectif du projet

Le **Chatbot Juridique Marocain** vise à :

- Fournir des **réponses automatisées** aux questions juridiques courantes ;
- Simplifier l’accès à l’information légale marocaine (Constitution, Code du travail, etc.) ;
- Aider les citoyens et professionnels à **comprendre leurs droits et obligations** ;
- Illustrer l’intégration d’un modèle de langage avancé dans une **application web complète**.

---

## 🏗️ Architecture générale

Le projet repose sur une architecture **client-serveur** moderne :
Frontend (HTML, CSS, JS)
│
▼
Backend (Flask - Python)
│
▼
IA & Base de connaissances (OpenAI API + JSON local)


---

## ⚙️ Choix technologiques

### 🔹 Backend

- **Langage** : Python  
- **Framework** : [Flask](https://flask.palletsprojects.com/)  
- **Bibliothèques principales** :
  - `Flask` : gestion du serveur web et des routes ;
  - `OpenAI` : interaction avec le modèle GPT-3.5-turbo ;
  - `dotenv` : gestion des variables d’environnement (clés API) ;
  - `re` : traitement de texte et expressions régulières.

### 🔹 Intelligence Artificielle (NLP)

Le cœur du chatbot repose sur un modèle de langage neuronal **GPT-3.5-turbo** via l’API OpenAI.  
Ce modèle :

- Comprend les **questions juridiques** posées en français ;
- Détecte les **articles de loi marocains** pertinents ;
- Génère des **réponses structurées et fiables**, dans le ton d’un expert juridique.

En complément, une **base de données locale JSON** a été construite à partir des textes marocains officiels (Constitution, Code du travail, etc.) afin de :

- Réduire la dépendance à l’API OpenAI ;
- Accélérer l’accès à certaines références légales.

### 🔹 Frontend

- **Technologies utilisées** : HTML, CSS, JavaScript  
- **Rôle** :
  - Interface intuitive permettant à l’utilisateur de poser ses questions ;
  - Communication asynchrone avec le backend via `fetch()` ou `AJAX` ;
  - Affichage dynamique des réponses juridiques.

---

## 🧩 Fonctionnement global

1. **L’utilisateur** saisit une question juridique via l’interface web.  
2. **Le serveur Flask** reçoit la requête et l’analyse.  
3. Si la question correspond à un article connu :
   - Le système extrait la réponse depuis la **base de données JSON locale**.  
4. Sinon :
   - La requête est envoyée au **modèle GPT-3.5-turbo** via l’API OpenAI.  
5. La **réponse générée** est renvoyée au frontend, puis affichée à l’utilisateur.

---

![Interface du Chatbot](static/images/interface_chatbot.png)


---

## 🚀 Installation et exécution

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/AbdoDbaibigh/legal-chatbot.git
cd chatbot-juridique
```

### 3️⃣ Configurer la clé API OpenAI

Créer un fichier .env à la racine du projet :
```bash
API_KEY=ta_cle_api_openai
```

### 4️⃣ Lancer le serveur Flask
```bash
python app.py
```