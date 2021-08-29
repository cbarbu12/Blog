from datetime import datetime
from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    textField = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()
    
    def approveComments(self):
        return self.comments.filter(approvedComment=True)

    def getAbsoluteUrl(self):
        return reverse("postDetail", kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length='50')
    text = models.TextField()
    cretedDate = models.DateTimeField(default=datetime.now())
    approvedComment = models.BooleanField(default=False)

    def approve(self):
        self.approvedComment = True
        self.save()
    
    def getAbsoluteUrl(self):
        return reverse('postList')

    def __str__(self):
        return self.text