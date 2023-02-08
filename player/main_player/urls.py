from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', video_list,name='video_list'),
    path('video/<slug:slug>/', video_page, name='video_page'),
    path('stream/<slug:slug>/', get_streaming_video, name='stream')
]
