from django.db import models
from django.contrib.auth.models import User
import uuid

class MovieRoom(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, default=uuid.uuid4().hex[:6].upper())
    host = models.ForeignKey(User, related_name='hosted_rooms', on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(User, related_name='rooms', blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(MovieRoom, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'
