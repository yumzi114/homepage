from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# from .managers import PersonManager

# Create your models here.


# class userprofile(models.Model):
#     avata_name=models.CharField('avataname', max_length=10, blank=False, null=False)
#     user_name=models.OneToOneField(User,on_delete=models.CASCADE, verbose_name='userid',blank=False, null=False)
#     class Meta:
#         db_table = "useravata"
#         ordering = ("user_name",)
class UserProfile(AbstractUser):
    avata_name=models.CharField('avataname', max_length=10, blank=False, null=False)
    class Meta:
        db_table = 'userprofile'
