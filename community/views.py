from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import ChatGroup, GroupMessage
from .serializers import ChatGroupSerializer, GroupMessageSerializer
from django.db.models import Q

class IsAdminOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or (hasattr(obj, 'admin') and obj.admin == request.user)

class IsAuthorOrAdminOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or (hasattr(obj, 'author') and obj.author == request.user) or (hasattr(obj, 'group') and hasattr(obj.group, 'admin') and obj.group.admin == request.user)

# View for listing, creating, and searching chat groups
class ChatGroupView(generics.ListCreateAPIView):
    queryset = ChatGroup.objects.all()
    serializer_class = ChatGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        search = self.request.query_params.get('search')
        qs = super().get_queryset()
        if search:
            qs = qs.filter(Q(group_name__icontains=search) | Q(groupchat_name__icontains=search))
        return qs

    def perform_create(self, serializer):
        group = serializer.save(admin=self.request.user)
        group.members.add(self.request.user)
        group.save()

# View for listing, creating, and deleting messages within a specific group
class GroupMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, group_id):
        group = get_object_or_404(ChatGroup, id=group_id)
        messages = GroupMessage.objects.filter(group=group).order_by('-created')
        serializer = GroupMessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, group_id):
        group = get_object_or_404(ChatGroup, id=group_id)
        serializer = GroupMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, group=group)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class GroupMessageDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrAdminOrSuperUser]

    def delete(self, request, message_id):
        message = get_object_or_404(GroupMessage, id=message_id)
        self.check_object_permissions(request, message)
        message.delete()
        return Response({'detail': 'Message deleted.'}, status=status.HTTP_204_NO_CONTENT)

class ChatGroupDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSuperUser]

    def delete(self, request, group_id):
        group = get_object_or_404(ChatGroup, id=group_id)
        self.check_object_permissions(request, group)
        group.delete()
        return Response({'detail': 'Group deleted.'}, status=status.HTTP_204_NO_CONTENT)
