from . import views     #current directory calling
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('xyz/', views.test),
    path('login/', views.log),
    path('reg/', views.reg),
    path('login/loginsub/', views.logsub),
    path('reg/registersub/', views.regsub),
]
