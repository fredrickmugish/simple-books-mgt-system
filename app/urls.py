from django.urls import path
from . import views

urlpatterns = [

path('hello/', views.hello),
path('', views.book),
path('add_book/', views.add_book),
path('add_book/add', views.addBook),
path('edit_book/', views.editBookView),
path('edit_book/edit', views.editBook),
path('delete_book/<int:pk>', views.deleteBook, name="delete_book")

]