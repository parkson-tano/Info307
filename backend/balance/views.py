from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from account.models import AccountBalance
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import generics
#  your views here.


class AccountBalanceViewAPI(viewsets.ModelViewSet):
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer


class DepositViewAPI(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class WithdrawViewAPI(viewsets.ModelViewSet):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer


class TransferViewAPI(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer


class AirtimeViewAPI(viewsets.ModelViewSet):
    queryset = Airtime.objects.all()
    serializer_class = AirtimeSerializer


class GetAccountBalanceViewAPI(viewsets.ModelViewSet):
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer


class GetDepositViewAPI(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = GetDepositSerializer


class GetWithdrawViewAPI(viewsets.ModelViewSet):
    queryset = Withdraw.objects.all()
    serializer_class = GetWithdrawSerializer


class GetTransferViewAPI(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = GetTransferSerializer


class GetAirtimeViewAPI(viewsets.ModelViewSet):
    queryset = Airtime.objects.all()
    serializer_class = GetAirtimeSerializer


@api_view(['GET'])
def history(request, number):
    deposit = Deposit.objects.filter(
        Q(recipient__phone_number=number) | Q(momo_agent__phone_number=number))
    withdraw = Withdraw.objects.filter(
        Q(user__phone_number=number) | Q(momo_agent__phone_number=number))
    transfer = Transfer.objects.filter(
        Q(sender__phone_number=number) | Q(receiver__phone_number=number))
    airtime = Airtime.objects.filter(
        Q(user__phone_number=number) | Q(number=number))

    deposit_serializer = GetDepositSerializer(
        deposit, many=True, context={'request': request})
    withdraw_serializer = GetWithdrawSerializer(
        withdraw, many=True, context={'request': request})
    transfer_serializer = GetTransferSerializer(
        transfer, many=True, context={'request': request})
    airtime_serializer = GetAirtimeSerializer(
        airtime, many=True, context={'request': request})
    data = deposit_serializer.data + withdraw_serializer.data + \
        transfer_serializer.data + airtime_serializer.data
    return Response(data)


@api_view(['GET', 'PATCH'])
def search(request, number):
    mtn_account = User.objects.get(phone_number=number)
    user_serializer = GetUserSerializer(
        mtn_account, context={'request': request})
    return Response(user_serializer.data)
