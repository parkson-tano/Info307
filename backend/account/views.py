from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# from django.contrib.auth import get_user_model
# User = get_user_model()


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserCreateViewAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class MtnAccountCreateViewAPI(generics.CreateAPIView):
    queryset = MtnAccount.objects.all()
    serializer_class = MtnAccountSerializer


class MtnAccountViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = MtnAccount.objects.all()
    serializer_class = MtnAccountSerializer


class AgentAccountCreateViewAPI(generics.CreateAPIView):
    queryset = AgentAccount.objects.all()
    serializer_class = AgentAccountSerializer


class MtnAccountView(generics.ListAPIView):
    queryset = MtnAccount.objects.all()
    serializer_class = MtnAccountSerializer


class AgentAccountView(generics.ListAPIView):
    queryset = AgentAccount.objects.all()
    serializer_class = AgentAccountSerializer

class AgentAccountViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentAccount.objects.all()
    serializer_class =AgentAccountSerializer

class LogoutAndBlacklistRefreshToken(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
