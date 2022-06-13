from django.db import models

from users.models import Profile

# Create your models here.


class NoticeType(models.TextChoices):
    NEW_POST = 'new_post'
    COMMENT = 'comment'
    CALENDAR = 'callendar'


class Notice(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile')
    notice_type = models.CharField(
        max_length=15, choices=NoticeType.choices, default=None)
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(
        max_length=20, default=None, blank=True, null=True)
    content = models.CharField(
        max_length=20, default=None, blank=True, null=True)

    def __str__(self):
        return self.notice_type + self.create_time.strftime("(%m/%d/%Y, %H:%M:%S)")
