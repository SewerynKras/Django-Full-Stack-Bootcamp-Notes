from django.urls import path
from registration import views


app_name = "registration"


urlpatterns = [
    # path("", views.),
    path("register/", views.RegisterView.as_view(), name='register')
]
