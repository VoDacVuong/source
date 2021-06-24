from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import models, user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'