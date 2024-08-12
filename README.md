# E-commerce site
### Why do we need this website?
This basic site used for sellers in any store. The website provides users to create categories or products. Users can reduce or increase quantity of their products. It means if seller sells a product in the site the amount of product is also reducible or if employees brings new products or more products that already exists in store, they can add new product or put up quantity to their product. This is why i created the website.
# How to launch and run
### Create virtualenv (in terminal):
##
<tab><tab>code/pip install pipenv 
##
<tab><tab>code/pipenv shell
### Configure database
##
<tab><tab>code/python manage.py makemigrations 
##
<tab><tab>code/python manage.py migrate `
### Install required packages
##
<tab><tab>code/pipenv install django 
##
<tab><tab>code/pipenv install Pillow  
### Create superuser
##
<tab><tab>code/python manage.py createsuperuser 
### Run project
##
<tab><tab>code/python manage.py runserver 
### Then click the url. The url: http://127.0.0.1:8000
### Enjoy and follow my other repositories(Optional)
