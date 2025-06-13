from django.db import models\
from cloudinary.models import CloudinaryField

# Create your models here
class items(models.Model):
    category_choices=[
        ('main','Main Dish'),
        ('side','Side Dish'),
        ('drink','Drinks'),
        ('snack','Snacks')
    ]

    image = CloudinaryField('image')
    title=models.CharField(max_length=100)
    description=models.TextField()
    Price=models.IntegerField()
    category=models.CharField(max_length=100,choices=category_choices)  
