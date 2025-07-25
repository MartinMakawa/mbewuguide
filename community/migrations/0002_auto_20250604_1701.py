# Generated by Django 3.2.25 on 2025-06-05 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(blank=True, max_length=128, unique=True)),
                ('groupchat_name', models.CharField(blank=True, max_length=128, null=True)),
                ('is_private', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groupchats', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, related_name='chat_groups', to=settings.AUTH_USER_MODEL)),
                ('users_online', models.ManyToManyField(blank=True, related_name='online_in_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, max_length=300, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='community.chatgroup')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
