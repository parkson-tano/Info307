from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
    phone_number = models.CharField(_('phone number'), unique=True, max_length=15)
    profile_pic = models.ImageField(upload_to="profile_pic", null=True, blank=True)
    momo_agent = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    
    def __str__(self):
        return "{}".format(self.phone_number)

class Verification(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_verification')
    id_num = models.CharField(max_length=18, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    front_pic = models.ImageField(upload_to='verification', null=True, blank=True)
    rear_pic = models.ImageField(upload_to='verification', null=True, blank=True)
    complete = models.BooleanField(default=False)


class AccountBalance(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_account')
    balance = models.FloatField(default=0)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        AccountBalance.objects.create(user=instance)



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Verification.objects.create(user=instance)
