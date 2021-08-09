from django.urls import path
from base_app import views

app_name = 'base_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'login')
]

