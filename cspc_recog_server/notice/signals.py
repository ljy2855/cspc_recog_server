from django.db.models.signals import post_save
from django.dispatch import receiver

from board.models import Post, Comment
from users.models import Profile
from .models import Notice, NoticeType

# 공지사항 생성 시 모든 유저에게 signal


@receiver(post_save, sender=Post)
def board_notice(sender, instance, created, **kwargs):
    if created == True:
        post = instance
        if post.is_notice:
            all_profiles = Profile.objects.all()
            for profile in all_profiles:
                Notice.objects.create(
                    profile=profile,
                    notice_type=NoticeType.NEW_POST
                )

# 댓글 작성시 원글 작성자에게 알림


@receiver(post_save, sender=Comment)
def comment_notice(sender, instance, created, **kwargs):
    if created == True:
        comment = instance
        noticed_profile = comment.post_id.author
        if noticed_profile != comment.author:  # 게시글과 댓글 작성자가 다를경우
            Notice.objects.create(
                profile=noticed_profile,
                notice_type=NoticeType.COMMENT,
            )
