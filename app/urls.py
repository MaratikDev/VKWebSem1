from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),       # главная страница

    path('ask/', views.ask),
    path('hot/', views.hot),
    path('login/', views.login),
    path('question/<int:question_id>', views.question),#
    path('register/', views.register),
    path('settings/', views.settings),
    path('tag/<str:tag_name>', views.tag),#
]
