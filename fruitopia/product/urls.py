from django.urls import path
from . import views     #current directory calling

urlpatterns = [
    path('',views.test1)
]

