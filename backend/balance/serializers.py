from rest_framework import serializers
from .models import *
from account.models import AccountBalance
from account.serializers import *


class AccountBalanceSerializer(serializers.ModelSerializer):
    user = GetUserSerializer(read_only=True)

    class Meta:
        model = AccountBalance
        fields = "__all__"

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBalance
        fields = "__all__"

class BalanceSerializer(serializers.ModelSerializer):
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


class GetDepositSerializer(serializers.ModelSerializer):
    recipient = GetUserSerializer(read_only=True)

    class Meta:
        model = Deposit
        fields = "__all__"


class GetWithdrawSerializer(serializers.ModelSerializer):
    user = GetUserSerializer(read_only=True)

    class Meta:
        model = Withdraw
        fields = "__all__"


class GetTransferSerializer(serializers.ModelSerializer):
    receiver = GetUserSerializer(read_only=True)
    sender = GetUserSerializer(read_only=True)
    class Meta:
        model = Transfer
        fields = "__all__"


class GetAirtimeSerializer(serializers.ModelSerializer):
    user = GetUserSerializer(read_only=True)

    class Meta:
        model = Airtime
        fields = "__all__"
