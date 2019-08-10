from django.urls import path
from posts import views


app_name = "posts"

urlpatterns = [
    path("", views.IndexView.as_view(), name='homepage'),
    path("new", views.NewPostView.as_view(), name='new_post'),
    path("drafts", views.DraftView.as_view(), name='drafts'),
    path("drafts/<slug>/edit", views.UpdateDraft.as_view(), name='edit_draft'),
    path("drafts/<slug>/publish", views.PublishDraft.as_view(), name='publish'),
    path("drafts/<slug>/delete", views.DeleteDraft.as_view(), name='delete'),
]
