from django.urls import path
from .views import register, login, forget_pwd

urlpatterns = [
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('forget_pwd/', forget_pwd, name = 'forget_pwd'),
]
