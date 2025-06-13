from django.db import models

# Create your models here
class items(models.Model):
    category_choices=[
        ('main','Main Dish'),
        ('side','Side Dish'),
        ('drink','Drinks'),
        ('snack','Snacks')
    ]

    image=models.ImageField(upload_to="items/")
    title=models.CharField(max_length=100)
    description=models.TextField()
    Price=models.IntegerField()
    category=models.CharField(max_length=100,choices=category_choices)  