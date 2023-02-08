from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from .services import *
from django.http import StreamingHttpResponse

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'main_player/video_list.html', {'videos': videos})

def video_page(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'main_player/video_page.html', {'video': video})

def get_streaming_video(request, slug):
    file, status_code, content_length, content_range = open_file(request, slug)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response