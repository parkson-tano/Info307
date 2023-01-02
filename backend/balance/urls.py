from django.urls import path
from .views import *
urlpatterns = [
    path("accountbalance", AccountBalanceViewAPI.as_view({'get': 'list',
                                                         'post': 'create'})),
    path("accountbalance/<int:pk>", GetAccountBalanceViewAPI.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path("deposit", DepositViewAPI.as_view({'get': 'list',
                                           'post': 'create'})),
    path("deposit/<int:pk>/", GetDepositViewAPI.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path("withdraw", WithdrawViewAPI.as_view({'get': 'list',
                                             'post': 'create'})),
    path("withdraw/<int:pk>", GetWithdrawViewAPI.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path("airtime", AirtimeViewAPI.as_view({'get': 'list',
                                           'post': 'create'})),
    path("airtime/<int:pk>/", GetAirtimeViewAPI.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path("transfer", TransferViewAPI.as_view({'get': 'list',
                                             'post': 'create'})),
    path("transfer/<int:pk>/", GetTransferViewAPI.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path('history/<number>', history),
    path('search/<number>', search),
]
