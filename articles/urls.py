from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [

    # 현재 articles 폴더 내에 있는 views.py를 import
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/delete/', views.delete, name='delete'),
]