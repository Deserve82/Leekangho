from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
