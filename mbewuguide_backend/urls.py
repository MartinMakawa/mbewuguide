# mbewuguide_backend/urls.py
from django.urls import include
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from crops.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('crops.urls')),  # this includes all routes from crops/urls.py,
    path('signup/', signup, name='signup'),  # Your custom signup view
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh
    path('api/community/', include('community.urls')),


]


