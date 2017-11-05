from django.db import models  
from django.contrib.auth.models import User
import uuid
from datetime import datetime  
# Create your models here.


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500 )
    content = models.CharField(max_length=2000)
    isPublished = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default = datetime.now)
    createdBy = models.ForeignKey(User, related_name="news_author")
    publishedAt = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return "{0} created by {1} at {2}".format(self.title , self.createdBy , self.createdAt)