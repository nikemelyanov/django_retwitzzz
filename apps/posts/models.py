from datetime import timedelta
from django.db import models

from apps.users.models import User

from django.utils import timezone

   
class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    body = models.TextField(null=True, blank=True)
    created_timestamp = models.DateTimeField(default=timezone.now() + timedelta(hours=3))

class PostComment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(null=True, blank=True)
    created_timestamp = models.DateTimeField(default=timezone.now() + timedelta(hours=3))
