from django.urls import path
from simple_app import views


app_name = "simple_app"

urlpatterns = [
    path("", views.IndexCBV.as_view(), name='homepage'),
    path("list/", views.SchoolListView.as_view(), name='list'),
    path("detail/<int:pk>", views.SchoolDetailView.as_view(), name='detail'),
]
