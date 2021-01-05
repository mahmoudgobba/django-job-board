from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_user')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=5000,null=True)
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/',blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_post',on_delete=models.CASCADE,null=True)
    text = models.TextField(max_length=256,null=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
