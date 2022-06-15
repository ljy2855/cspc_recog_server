from turtle import title
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
        notice_title = "새로운 공지가 올라왔어요!"
        notice_content = post.contents
        if post.is_notice:
            all_profiles = Profile.objects.all()
            for profile in all_profiles:
                Notice.objects.create(
                    profile=profile,
                    notice_type=NoticeType.NEW_POST,
                    title=notice_title,
                    content=notice_content,
                    related_post=post,
                )

# 댓글 작성시 원글 작성자에게 알림


@receiver(post_save, sender=Comment)
def comment_notice(sender, instance, created, **kwargs):
    if created == True:
        comment = instance
        notice_title = comment.author.nick_name + "님이 댓글을 남겼어요!"
        notice_content = comment.contents
        noticed_profile = comment.post_id.author
        if noticed_profile != comment.author:  # 게시글과 댓글 작성자가 다를경우
            Notice.objects.create(
                profile=noticed_profile,
                notice_type=NoticeType.COMMENT,
                title=notice_title,
                content=notice_content,
                related_post=comment.post_id,
            )
