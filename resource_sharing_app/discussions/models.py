from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Discussion(models.Model):
    discussion_id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"Comment by {self.author} on {self.discussion.title}"
