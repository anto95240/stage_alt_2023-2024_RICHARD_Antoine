# Nom du Projet

## Description
Ce projet est une plateforme pédagogique développée avec Django et Vue.js. Il vise à fournir un environnement où les utilisateurs peuvent s'inscrire, se connecter et accéder à des fonctionnalités administratives et pédagogiques.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé les éléments suivants :
- [Python 3.11](https://www.python.org/downloads/)
- [Node.js] et [npm](https://nodejs.org/en/download/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Installation

### Backend (Django)

1. Clonez ce dépôt :
   ```bash
   git clone <lien-du-depot>
   cd backend

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate  # Windows

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt

4. Appliquez les migrations :
    ```bash
    python manage.py migrate

5. Lancez le serveur Django :  
    ```bash
    python manage.py runserver

###	Frontend (Vue.js)
1. Accédez au répertoire frontend :
    ```bash
    cd ../frontend

2. Installez les dépendances :
    ```bash
    npm install

3. Lancez le serveur de développement Vue.js :
    ```bash
    npm run serve

## Utilisation
Une fois que les serveurs backend et frontend sont en cours d'exécution, vous pouvez accéder à l'application en visitant `http://localhost:8080` dans votre navigateur.

