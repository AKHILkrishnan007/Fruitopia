from . import views,feed     #current directory calling
from django.urls import path

urlpatterns = [
    path('', views.index,name='homepage'),
    path('xyz/', views.test),
    path('login/', views.log),
    path('reg/', views.reg),
    path('login/loginsub/', views.logsub),
    path('reg/registersub/', views.regsub),
    path('logout/', views.logout),
    path('feed/', feed.latest()),
    path('search/', views.sch),
    path('search/searchsub/', views.schsub),
    
]
