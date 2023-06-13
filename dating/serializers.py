from rest_framework import serializers
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import Lover

class LoverSerializer(serializers.Serializer):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True, validators=[username_validator])
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=1, choices=Lover.GENDER_CHOICES, verbose_name='Пол')
    photo = models.ImageField(upload_to="members/", verbose_name="Фото")