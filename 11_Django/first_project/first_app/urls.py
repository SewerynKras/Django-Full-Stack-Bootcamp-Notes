from django.urls import path
from first_app import views

urlpatterns = [
    path("", views.nested),
    path("img", views.image)
]
