#Question
"""
7. Explain what a Django project is
"""
#solution
print("--------------------------------------")

Django Project is a full web app where settings.py , urls.py , view.py means it will be a full web app that contain full webapp configuration and full setup

#Question
"""
8. Create a Django project
"""
#solution
print("--------------------------------------")

first activate venv , then install django in venv. then create this project

python -m venv venv
venv/Scripts/activate
pip install django
django-admin startproject myproject .


#Question
"""
9. Start the Django development server
"""
#solution
print("--------------------------------------")

python manage.py runserver

#Question
"""
10. Explain Browser → URL → View → Response
"""
#solution
print("--------------------------------------")


Brower/client will be send the request to django , django check the request url in urls.py then check ,find and if get then redirect to that request url and for showing data it use the view.py file it will be the model that is the responsible for showing data on screen, and after that django response to browser as per request (like client searching for about page . django go through url.py search for url if found then it will go to view.py for content then return the response as data in ui screen in browser)



