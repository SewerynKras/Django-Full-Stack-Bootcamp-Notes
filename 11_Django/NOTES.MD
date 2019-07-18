# Notes on different parts of the Django section

## Creating projects

use `$ django-admin startproject "projectname"` to start a new project\
use `$ python manage.py startapp "appname"` to create a new app

## Views

Views manage what gets displayed back to the user. Different apps will have their own views.py files.

## Urls

Different apps will have their own url mappings. These need to be connected to the projects urls.py. This can be done by modifying the 'projectname/urls.py' by adding `include("appname.urls")` to the urlpatterns

## Templates

Each app can have its own template in the 'templates/' directory. The directory itself needs to be added to projectname/settings.py To insert any content from outside the html file you need to add `{{ some_name }}` to the html and then
use `render(request, path_to_template.html, {"some_name":"some message"})`

## Static files

Static files are files that should never change (images, css, scripts etc) and can be loaded into html by using `{% load staticfiles %}`. To use a static file inside html you should use `"{% static "filename.png" %}"`. Static files should be stored in a separate directory and that dir should be added to projectname/settings.py
