from django.urls import path
from infolotapp import views

urlpatterns = [
    path('', views.home),
    path('signup', views.signup),
    path('login', views.login),
]