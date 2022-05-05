from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    # Головачная страница
    path('', views.index, name = 'main'),
    # Основная работа ведется здесь
    path('group/<slug:slug>/', views.group_posts, name = 'group_list')
]