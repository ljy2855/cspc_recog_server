from django.db import models
from users.models import Group, Profile
from django.contrib.auth.models import User
# Create your models here.


class Board(models.Model):
    board_name = models.CharField(max_length=10)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)


class Post(models.Model):
    board_id = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='board', default='')
    title = models.CharField(max_length=30, null=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    contents = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    like_count = models.IntegerField(default=0)
    like_members = models.ManyToManyField(
        Profile, related_name='like_post', blank=True)
    has_image = models.BooleanField(default=False)
    is_notice = models.BooleanField(default=False)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 이미지 업로드 날짜에 따라 디렉토리에 저장
    image = models.ImageField(upload_to='post/%y/%m/%d')


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    #author = models.CharField(max_length=10, null=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    contents = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
