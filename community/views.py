from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import ChatGroup, GroupMessage
from .serializers import ChatGroupSerializer, GroupMessageSerializer

# View for listing and creating chat groups
class ChatGroupView(generics.ListCreateAPIView):
    queryset = ChatGroup.objects.all()
    serializer_class = ChatGroupSerializer

# View for listing and creating messages within a specific group
class GroupMessageView(APIView):
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
