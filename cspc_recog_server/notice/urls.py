from django.urls import path
from .views import *

app_name = 'notice'

urlpatterns = [
    path('profile=<int:profile_id>/', NoticeListAPI.as_view()),
    path('id=<int:notice_id>/', NoticeAPI.as_view())
]
