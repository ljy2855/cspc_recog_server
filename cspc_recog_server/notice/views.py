from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from notice.models import NoticeType
from notice.models import Notice
from notice.serializers import NoticeSerializer


class NoticeListAPI(APIView):
    def get(self, request, **kwargs):
        profile_id = kwargs.get('profile_id')
        if profile_id is None:
            return Response(status=400)
        else:
            notice_serializer = NoticeSerializer(
                Notice.objects.filter(profile=profile_id), many=True)
            return Response(notice_serializer.data, status=200)


class NoticeAPI(APIView):
    def get(self, request, notice_id):
        notice = get_object_or_404(Notice, id=notice_id)
        if notice.notice_type != NoticeType.CALENDAR:
            serializer = NoticeSerializer(notice)
            return Response(serializer.data, status=200)

    def delete(self, request, notice_id):
        notice = get_object_or_404(Notice, id=notice_id)
        notice.delete()
        return Response("delete success", status=200)


# Create your views here.
