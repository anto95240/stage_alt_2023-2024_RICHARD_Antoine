# EduCool

## Description
EduCool est une plateforme pédagogique développée avec Django (Backend) et Vue.js (Frontend). Elle permet aux utilisateurs de s'inscrire, se connecter, et accéder à des fonctionnalités administratives et pédagogiques.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé les éléments suivants :
- [Python 3.11](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/fr/)
- [WampServer (pour windows)](https://wampserver.aviatechno.net/) ou [Mamp (pour mac)](https://www.mamp.info/en/downloads/)

## Installation

### Base de Donnée (MySql)

1. Ouvrez WampServer ou Mamp selon votre système d'exploitation.

2. Accédez à PhpMyAdmin depuis l'interface de WampServer ou Mamp.

3. Connectez-vous avec les identifiants suivants :
   - WampServer : Nom d'utilisateur : "root", Pas de mot de passe.
   - Mamp : Nom d'utilisateur : "root", Mot de passe : "root".

4. Créez une nouvelle base de données nommée : education_platform.
   
5. Si vous utilisez Mamp, modifiez la configuration dans le fichier settings.py de la partie backend pour ajouter le mot de passe dans la section DATABASES.

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

5. Créez un superutilisateur (pour l'accès à l'admin de Django) :
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

Pour accéder à l'interface d'administration de Django, visitez http://localhost:8000/admin et connectez-vous avec les informations du superutilisateur créées à l'étape 5 du backend.

### Autre informations utiles
Il peut y avoir un problème lors de la déconnexion. Pour résoudre cela :
1. Ouvrez l'inspecteur de votre navigateur (clic droit → Inspecter).
2. Allez dans l'onglet "Application".
3. Sous la section "Storage", développez "Cookies" et sélectionnez le lien du site.
4. Supprimez les cookies "csrftoken" et "sessionid".
5. Vous pourrez maintenant vous déconnecter correctement.
