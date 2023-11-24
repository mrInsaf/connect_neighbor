# accounts/urls.py
from django.urls import path
from .views import signup, signin, home

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('home/', home, name='home'),
]
