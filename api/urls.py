from django.urls import path
from . import views

urlpatterns = [
    path('book/create/', views.book_create, name='create-book'),
    path('book/retrive/', views.book_retrive, name='retrive-book'),
    path('book/update/', views.book_update, name='update-book'),
    path('book/delete/', views.book_delete, name='delete-book'),
]
