from django.urls import path
from . import views     #current directory calling

urlpatterns = [
    path('',views.details2,name='prod'),
    path('cmt/',views.cmt),
    path('like/',views.like),
    path('autoc/',views.autoc,name='autocmplt'),
    
]

