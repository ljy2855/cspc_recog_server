from django.urls import path
from .views import *

app_name = 'notice'

urlpatterns = [
    path('<int:profile_id>', NoticeAPI.as_view())
]
