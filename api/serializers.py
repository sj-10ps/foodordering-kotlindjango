from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=items
        fields="__all__"
