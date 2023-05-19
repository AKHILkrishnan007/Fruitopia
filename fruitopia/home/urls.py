from . import views,feed     #current directory calling
from django.urls import path

urlpatterns = [
    path('', views.index,name='homepage'),
    path('xyz/', views.test),
    path('login/', views.log, name='loginpage'),
    path('reg/', views.reg, name='register'),
    # path('reg/registersub/', views.regsub),
    path('logout/', views.logout),
    path('feed/', feed.latest()),
    path('search/', views.sch),
    path('search/searchsub/', views.schsub),
    
]
