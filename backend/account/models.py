from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
from django.utils.translation import gettext as _


class User(AbstractUser):
	username = models.CharField(max_length=50, blank=True, null=True, unique=False, default="")
	phone_number = models.CharField(_('phone number'), unique=True, max_length=15)
	profile_pic = models.ImageField(
		upload_to="profile_pic", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	USERNAME_FIELD = 'phone_number'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def __str__(self):
		return "{}".format(self.phone_number)
