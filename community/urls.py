from django.urls import path
from .views import ChatGroupView, GroupMessageView, GroupMessageDeleteView, ChatGroupDeleteView

urlpatterns = [
    path('chat-groups/', ChatGroupView.as_view(), name='chat-group-list-create'),
    path('chat-groups/<int:group_id>/messages/', GroupMessageView.as_view(), name='group-message-list-create'),
    path('chat-groups/<int:group_id>/delete/', ChatGroupDeleteView.as_view(), name='chat-group-delete'),
    path('messages/<int:message_id>/delete/', GroupMessageDeleteView.as_view(), name='group-message-delete'),
]
