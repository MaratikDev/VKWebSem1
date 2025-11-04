from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),       # главная страница
    #path('base/', views.base), # пример другой страницы
    #path('index/', views.index) # пример другой страницы
]
