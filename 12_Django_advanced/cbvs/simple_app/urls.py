from django.urls import path
from simple_app import views


app_name = "simple_app"

urlpatterns = [
    path("", views.IndexCBV.as_view(), name='homepage'),
    path("list/", views.SchoolListView.as_view(), name='list'),
    path("detail/<int:pk>", views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.StudnetCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.StudentDeleteView.as_view(), name='delete'),
]
