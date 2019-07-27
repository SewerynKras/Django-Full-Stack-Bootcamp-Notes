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

## Models

Models are OOP versions of SQL database elements. They can be defined in appname/models.py and registered using appname/admin.py. However to apply these changes you must migrate the database using\
`$ python manage.py migrate`\
`$ python manage.py makemigrations "appname"`\
`$ python manage.py migrate`

## Forms

You can also define forms using python classes. These can be defined in appname/forms.py abd can be loaded into html same way like you'd load any other context using a template.

## Template inheritance (blocks)

To avoid copying the same lines of code to multiple html files (like navbar or loading bootstrap etc) you can just define a single file and call it in other html documents. You can mark everything as reusable in a file using a pair of `{% block block_name %}` and `{% endblock %}`
(This will mark everything **outside** the blocks)\
To later use that marked code use `{% extends 'path_to_file' %}'`

## Users

It's generally not a good idea to overwrite djangos user models with your own. Instead to add more functionality to them you can create custom models with `user = OneToOneField(User)`.

## Logins

Django has pretty sweet built-in support for authentication. When creating a view that should only be access when logged in you can use a decorator `@login_required()`
