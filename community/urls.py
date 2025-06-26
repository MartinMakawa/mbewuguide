from django.urls import path
from .views import ChatGroupView, GroupMessageView

urlpatterns = [
    path('chat-groups/', ChatGroupView.as_view(), name='chat-group-list-create'),
    path('chat-groups/<int:group_id>/messages/', GroupMessageView.as_view(), name='group-message-list-create'),
]
