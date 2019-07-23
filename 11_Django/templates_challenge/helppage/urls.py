from django.urls import path
from helppage.views import helppage

urlpatterns = [
    path("", helppage)
]
