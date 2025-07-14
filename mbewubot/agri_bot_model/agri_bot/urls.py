from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('ask/', views.ask_question, name='ask_question'),
    path('search/', views.search_content, name='search_content'),
    path('history/', views.get_history, name='get_history'),
    path('model-info/', views.model_info, name='model_info'),
] 