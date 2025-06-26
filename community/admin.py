from django.contrib import admin
from .models import ChatGroup, GroupMessage

class GroupMessageInline(admin.TabularInline):
    model = GroupMessage
    extra = 0

class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'groupchat_name', 'admin', 'is_private')
    inlines = [GroupMessageInline]

class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ('group', 'author', 'body', 'created')
    list_filter = ('group', 'author')

admin.site.register(ChatGroup, ChatGroupAdmin)
admin.site.register(GroupMessage, GroupMessageAdmin)