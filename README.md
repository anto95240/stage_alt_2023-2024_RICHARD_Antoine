# EduCool

## Description
Ce projet est une plateforme pédagogique développée avec Django et VueJs. Il vise à fournir un environnement où les utilisateurs peuvent s'inscrire, se connecter et accéder à des fonctionnalités administratives et pédagogiques.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé les éléments suivants :
- [Python 3.11](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/fr/)
- [WampServer (si vous êtes sur windows)](https://wampserver.aviatechno.net/) ou [Mamp (si vous êtes sur mac)](https://www.mamp.info/en/downloads/)

## Installation

### Base de Donnée (MySql)

1. Ouvrez WampServer ou Mamp

2. Puis allez dans PhpMyAdmin depuis l'interface de WampServer ou Mamp

3. Connectez-vous avec les identifants :
- Pour WampServer : le nom d'utilisateur est "root" (sans les guillemets) et il n'y a pas de mot de passe
- Pour Mamp : le nom d'utilisateur est "root" (sans les guillemets) et le mot de passe est "root" (sans les guillemets)

4. Créez une nouvelle base de donnée avec comme nom : education_platform

5. Si vous utilisez Mamp, modifié dans le fichier settings, de back_side, la partie DATABASES en rajoutant le mot de passe

### Backend (Django)

1. Clonez ce dépôt :
   ```bash
   git clone <lien-du-depot>
   cd backend

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # si vous êtes sur macOS/Linux
    .venv\Scripts\activate  # si vous êtes sur Windows

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt

4. Appliquez les migrations :
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. Créez un superutilisateur (pour la partie admin de Django) :
    ```bash
    python manage.py createsuperuser

6. Lancez le serveur Django :  
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

Et pour accéder à l'admin de Django, visitez `http://localhost:8000/admin` dans votre navigateur et connectez-vous avec les informations d'identification du superutilisateur que vous avez crées à l'étape 5 de la partie BackEnd.


### Autre informations utiles
Il y a quelque soucis lors de la déconnexion, pour cela il faut aller dans l'inspecteur de votre navigateur (clic droit -> inspecter), dans l'onglet "Application" et supprimer le cookie "csrftoken" et "sessionid" puis on peut se déconnecter.
