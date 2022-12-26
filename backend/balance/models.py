from django.db import models
from account.models import User

# Create your models here.


class Deposit(models.Model):
    momo_agent = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_agent')
    recipient = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_receive')
    amount = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    type_transact = models.CharField(max_length=23, default='deposit', editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

class Transfer(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='user_sender')
    receiver = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='user_receiver')
    amount = models.IntegerField(default=0)
    fee = models.FloatField(default=0)
    complete = models.BooleanField(default=False)
    type_transact = models.CharField(
        max_length=23, default='transfer', editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

class Withdraw(models.Model):
    momo_agent = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_momo_agent')
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_withdraw')
    amount = models.IntegerField(default=0)
    fee = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    type_transact = models.CharField(
        max_length=23, default='withdraw', editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

class Airtime(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_credit')
    number = models.CharField(max_length=15)
    amount = models.IntegerField(default=0)
    type_transact = models.CharField(
        max_length=23, default='airtime', editable=False)
    date_created = models.DateTimeField(auto_now_add=True)


