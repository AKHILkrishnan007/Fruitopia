from django.urls import path
from . import views     #current directory calling

urlpatterns = [
    path('',views.details),
    path('cmt/',views.cmt),
    path('like/',views.like),
    
]

