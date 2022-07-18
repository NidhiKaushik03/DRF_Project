from django.db import models
from rest_framework import serializers
# Create your models here.

class Information(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    duration= models.FloatField()

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields ="__all__"
