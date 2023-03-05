# Json-Web-Token-with-Django-API
Implementation of JWT with permission to secure endpoint with Django/DRF
language: Eng/FR

-------------------------------------------------------------------------

To test and remember : 

create an environnement from your command-line in the folder you want/creer un environnement depuis le cmd dans un dossier

>> python -m venv <name_of_environnement>

# Then activate that environment/Activer l'environnement créé : 
"./<name_of_environnement>/Scripts/activate"

# Clone the repository/ Cloner le depot:
git clone https://github.com/IlemLembo/Json-Web-Token-with-Django-API.git

# Install the package from the requirements.txt file/ Installer les packages depuis le ficher requirements.txt :

first move to the your cloned directory then run/ aller dans le dossier cloné et installer entrer dans la ligne de commande:

pip install -r requirements.txt

# Run the Server/ Lancer le serveur :

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


# You can use Insomnia or Postman to test the Api!
# You can switch to the code, It' s full of comment!

happy coding
