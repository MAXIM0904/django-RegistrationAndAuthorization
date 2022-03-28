from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user_profile = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='user_profile')
    field_about_yourself = models.TextField(null=True, blank=True, verbose_name='О себе')
    avatar_user_img = models.ImageField(upload_to='images/', verbose_name='Аватар профиля', null=True, blank=True)

    def __str__(self):
        return str(self.user_profile)
