from django.urls import path
from .views import *
urlpatterns = [
    path("accountbalance", AccountBalanceCreateViewAPI.as_view()),
    path("accountbalance/<int:pk>", AccountBalanceViewAPI.as_view()),
    path("deposit", DepositCreateViewAPI.as_view()),
    path("deposit/<int:pk>/", DepositViewAPI.as_view()),
    path("withdraw", WithdrawCreateViewAPI.as_view()),
    path("withdraw/<int:pk>", WithdrawViewAPI.as_view()),
    path("airtime", AirtimeCreateViewAPI.as_view()),
    path("airtime/<int:pk>/", AirtimeViewAPI.as_view()),
]
