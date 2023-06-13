from rest_framework import serializers
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import User
from .models import Lover

class ProfileSerializer(serializers.Serializer):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True, validators=[username_validator])
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=1, choices=Lover.GENDER_CHOICES, verbose_name='Пол')
    photo = models.ImageField(upload_to="members/", verbose_name="Фото")


class LoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lover
        fields = '__all__'