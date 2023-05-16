from django.contrib.syndication.views import Feed
from django.db.models.base import Model
from django.template.defaultfilters import truncatewords
from product.models import fruits
from django.urls import reverse
from django.shortcuts import render,redirect

#feeds page

class latest(Feed):
    title='Fruitopia'
    link='/drcommments/'
    description='fruit shop for fresh fruits'

    def items(self):
        return fruits.objects.all()[:5]
    
    def item_title(self,data):
        return data.name
    
    def item_description(self,data):
        return truncatewords(data.desc,5)
    
    def item_link(self,data):
        return reverse('homepage')