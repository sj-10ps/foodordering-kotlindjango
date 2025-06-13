from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
path('',home,name='name'),
path('upload_items/',upload_items,name='upload_items'),
path("homepage",homepage,name="homepage"),
path("delete_items/",delete_items,name="delete_items"),
path("delete/<int:item_id>",delete,name="delete"),

path("manage_orders",manage_orders,name="manage_orders"),
]
