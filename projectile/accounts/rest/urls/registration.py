from django.urls import path 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.rest.views.registration import UserRegistration

urlpatterns = [
    path("/signup", UserRegistration.as_view(), name="user-signup"),
    path("/token", TokenObtainPairView.as_view(), name="pair-token"),
    path("/token/refresh", TokenRefreshView.as_view(), name="refresh-token"),
]
