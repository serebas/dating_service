from django.db import models
from django.contrib.auth.models import User

class Lover(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    photo = models.ImageField(upload_to="members/", verbose_name="Фото")

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'