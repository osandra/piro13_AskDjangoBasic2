from django.db import models
# Create your models here.
from .utils import uuid_upload_to
class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # tag_set = models.ManyToManyField('Tag', blank=True)  # Tag class가 아래 위치하니 문자열 안에 넣어줘라. blank=True는 tag지정 안해도 등록되게
    photo = models.ImageField(upload_to=uuid_upload_to)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Post 삭제되면 코멘트도 자동 삭제
    comment_message = models.TextField()


# class Tag(models.Model):
#     name = models.CharField(max_length=100, unique=True)