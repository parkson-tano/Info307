from django.urls import path
from .views import *
urlpatterns = [
    path("accountbalance", AccountBalanceViewAPI.as_view({'get': 'list',
                                                         'post': 'create'})),
    path("accountbalance/<int:pk>", AccountBalanceViewAPI.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path("deposit", DepositViewAPI.as_view({'get': 'list',
                                           'post': 'create'})),
    path("deposit/<int:pk>/", DepositViewAPI.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path("withdraw", WithdrawViewAPI.as_view({'get': 'list',
                                             'post': 'create'})),
    path("withdraw/<int:pk>", WithdrawViewAPI.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path("airtime", AirtimeViewAPI.as_view({'get': 'list',
                                           'post': 'create'})),
    path("airtime/<int:pk>/", AirtimeViewAPI.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path("transfer", TransferViewAPI.as_view({'get': 'list',
                                             'post': 'create'})),
    path("transfer/<int:pk>/", TransferViewAPI.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path('history/<number>', history),
]
