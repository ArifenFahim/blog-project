from django.urls import path, include
from .import views

app_name = "author"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='user_logout'),
]