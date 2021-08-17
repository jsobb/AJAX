from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('first/', first, name="first"),
    path('<int:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('posts/', posts, name="posts"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('<int:blog_id>/create_comment', create_comment, name="create_comment"),
    path('<int:blog_id>/<int:comment_id>/edit_comment', edit_comment, name="edit_comment"), 
    path('<int:blog_id>/<int:comment_id>/update_comment', update_comment, name="update_comment"), 
    path('<str:comment_id>/delete_comment', delete_comment, name="delete_comment"), 
    # 1. like_toggle url 연결하기
    path('<int:blog_id>/like_toggle', like_toggle,name='like_toggle'),
    path('<int:blog_id>/dislike_toggle', dislike_toggle,name='dislike_toggle'),
    
]
