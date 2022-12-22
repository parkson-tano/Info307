from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from account.models import AccountBalance, Verification
# Create your views here.

class AccountBalanceCreateViewAPI(generics.ListCreateAPIView):
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer


class AccountBalanceViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer


class VerificationCreateViewAPI(generics.ListCreateAPIView):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer


class VerificationViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer

class DepositCreateViewAPI(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class DepositViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class WithdrawCreateViewAPI(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer


class WithdrawViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer


class TransferCreateViewAPI(generics.ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer


class TransferViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer


class AirtimeCreateViewAPI(generics.ListCreateAPIView):
    queryset = Airtime.objects.all()
    serializer_class = AirtimeSerializer


class AirtimeViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airtime.objects.all()
    serializer_class = AirtimeSerializer
