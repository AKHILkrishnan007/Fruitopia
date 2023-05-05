from django.db import models

# Create your models here.
class fruits(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    price=models.IntegerField()
    qty=models.IntegerField()
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

class comment(models.Model):
    pro_id=models.ForeignKey(fruits,related_name='cmt',on_delete=models.CASCADE)
    
    user=models.CharField(max_lenth=100)
    msg=models.TextField()
    like=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)

