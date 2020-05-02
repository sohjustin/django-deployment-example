from django.urls import path
from . import views

app_name = 'AppTwo'

urlpatterns = [
    path('users_info/', views.users_info_page, name = 'users_info'),
    path('users/', views.users_page, name = 'users'),
    path('sign_in/', views.sign_in_page, name = 'sign_in'),
    path('register/', views.register , name = 'register'),
    path('user_login/', views.user_login, name = 'user_login'),
]
