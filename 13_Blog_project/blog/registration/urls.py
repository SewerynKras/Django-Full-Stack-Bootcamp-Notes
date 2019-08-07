from django.urls import path
from registration import views


app_name = "registration"


urlpatterns = [
    # path("", views.),
    path("register/", views.RegisterView.as_view(), name='register'),
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path("profile/<slug>", views.ProfileView.as_view(), name='profile')
]
