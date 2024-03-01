from django.urls import path
from .views import check
from .views import VideoDownload, VideoData

urlpatterns = [
    path("check/", check, name="check"),
    path("video/", VideoDownload.as_view(), name="download_video"),
    path("video/data/", VideoData.as_view(), name="video_data")
]
