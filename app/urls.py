from django.urls import path
from . import views

urlpatterns = [

path('hello/', views.hello),
path('', views.book),
path('add_book/', views.add_book),
path('add_book/add', views.addBook)

]