from rest_framework import serializers
from .models import ChatGroup, GroupMessage
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ChatGroupSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    admin = UserSerializer(read_only=True)
    # description = serializers.CharField(required=False, allow_blank=True)  # Uncomment if you add to model

    class Meta:
        model = ChatGroup
        fields = ['id', 'group_name', 'groupchat_name', 'admin', 'members', 'is_private'] # add 'description' if you add to model

class GroupMessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    group = ChatGroupSerializer(read_only=True)

    class Meta:
        model = GroupMessage
        fields = ['id', 'group', 'author', 'body', 'file', 'created']