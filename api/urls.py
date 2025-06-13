from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
path('registration/',registration,name='registration'),
path( 'login/',login,name=" login"),
path('update/',update,name='update'),
path('getitems/',getitems,name='getitems'),
path('addtocart/',addtocart,name='addtocart'),
path('cartdetails/',cartdetails,name='cartdetails'),
path('addtoorders/',addtoorders,name='addtoorders'),
path('getOrdereditems/',getOrdereditems,name='getOrdereditems'),
path('retrieveorderprogress/',retrieveorderprogress,name="retrieveorderprogress")



]
