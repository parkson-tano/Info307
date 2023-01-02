from rest_framework import serializers
from .models import *
from account.models import AccountBalance
from account.serializers import GetUserSerializer
class AccountBalanceSerializer(serializers.ModelSerializer):
    user = GetUserSerializer(read_only=True)
    class Meta:
        model = AccountBalance
        fields = "__all__"



class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = "__all__"


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = "__all__"


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = "__all__"


class AirtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airtime
        fields = "__all__"
