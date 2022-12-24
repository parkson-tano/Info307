from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("", UserCreateViewAPI.as_view(), name='user_create'),
    path("<int:pk>", UserApiView.as_view(), name='user_api'),
    path("mtn-account/<int:pk>", MtnAccountViewAPI.as_view()),
    path("agent-account/<int:pk>", AgentAccountViewAPI.as_view()),

    path("mtn-account", MtnAccountView.as_view()),
    path("agent-account", AgentAccountView.as_view()),

    path('register/', RegisterView.as_view(), name='auth_register'),
    path('register-mtn/', MtnAccountCreateViewAPI.as_view(), name='auth_register-mtn'),
    path('register-agent/', AgentAccountCreateViewAPI.as_view(), name='auth_register-agent'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutAndBlacklistRefreshToken.as_view(), name='blacklist_token'),
]
