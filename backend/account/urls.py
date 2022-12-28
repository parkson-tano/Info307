from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("", GetUserViewAPI.as_view({'get': 'list'}), name='user_create'),
    path("<int:pk>", UserViewAPI.as_view({'get': 'retrieve', 'put': 'update',
                                          'patch': 'partial_update',
                                          'delete': 'destroy'}), name='user_api'),
    path("mtn-account/<int:pk>", MtnAccountViewAPI.as_view({'get': 'retrieve', 'put': 'update',
                                                            'patch': 'partial_update',
                                                            'delete': 'destroy'})),
    path("agent-account/<int:pk>",
         AgentAccountViewAPI.as_view({'get': 'retrieve', 'put': 'update',
                                      'patch': 'partial_update',
                                      'delete': 'destroy'})),
    path("mtn-account", MtnAccountViewAPI.as_view({'get': 'list'})),
    path("agent-account",
         GetAgentAccountViewAPI.as_view({'get': 'list'})),

    path('register/',
         RegisterView.as_view({'post':'create'}), name='auth_register'),
    path('register-mtn/',
         MtnAccountViewAPI.as_view({'post': 'create'}), name='auth_register-mtn'),
    path('register-agent/',
         AgentAccountViewAPI.as_view({'post': 'create'}), name='auth_register-agent'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutAndBlacklistRefreshToken.as_view(), name='blacklist_token'),
    path('change_password/<int:number>/', ChangePasswordView.as_view(),
         name='auth_change_password'),
]
