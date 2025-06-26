# crops/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .auth_views import register_user
from .views import crop_recommendation  # already exists

urlpatterns = [
    path('recommend/', crop_recommendation, name='crop_recommendation'),
    path('register/', register_user, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
