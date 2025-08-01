"""
URL configuration for agri_bot_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('agri_bot.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
] 