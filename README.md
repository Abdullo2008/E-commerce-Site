# Create virtualenv (in terminal):
pip install pipenv
pipenv shell
# Configure database
python manage.py makemigrations
python manage.py migrate
# Install required packages
pipenv install django
pipenv install Pillow
# Create superuser
python manage.py createsuperuser
