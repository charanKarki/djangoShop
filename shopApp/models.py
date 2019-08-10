from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
def create_filename(instance,filename):
    ext = filename.split('.')[-1]
    
    filename = f'shoo.{ext}'
    return os.path.join('item/',filename)

class products(models.Model):
    itemsize_choices=[('6','6'),('7','7'),('8','8'),('9','9'),('10','10')]
    itemName  = models.CharField(max_length = 40)
    itemSize = models.CharField(max_length = 5,choices=itemsize_choices)
    itemImg = models.ImageField(upload_to = create_filename)
    discription= models.TextField(null= True)
    
    def __str__(self):
        return f'productId{self.id}'
    
class userProducts(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    productId = models.ForeignKey(products,on_delete =models.CASCADE)

    def __str__(self):
        return f'{self.userId.username} product {self.productId.itemName }'
