from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from rest_framework.views import APIView
from .serializer import VideoRequestSerializer

from pytube import YouTube

import datetime

# Create your views here.


def check(request):
    return JsonResponse({"response": "OK!", "date": datetime.datetime.now(), "user": "Generic"})


class VideoData(APIView):
    def get(self, request):
        video_request_serializer = VideoRequestSerializer(data=request.data)
        if video_request_serializer.is_valid():
            url = video_request_serializer.validated_data.get("url")

            yt = YouTube(url)

            return JsonResponse({"videos": [{"id": video.itag, "title": video.title, "resolution": video.resolution, "fps": video.fps, "format": video.mime_type[6::]} for video in yt.streams.filter(adaptive=True, only_video=True).all()]})

        return JsonResponse({"response": "Error!", "date": datetime.datetime.now(), "user": "Generic", "errors": video_request_serializer.errors})


class VideoDownload(APIView):
    def get(self, request):
        video_request_serializer = VideoRequestSerializer(data=request.data)
        if video_request_serializer.is_valid():
            url = video_request_serializer.validated_data.get("url")

            yt = YouTube(url)

            stream = yt.streams.filter(
                progressive=True, file_extension="mp4", res="720p").first()

            stream.download(output_path="./media/video/",
                            filename=stream.title)

            response = FileResponse(open(
                "./media/video/" + stream.title, "rb"), as_attachment=True, content_type="video/mp4")
            response["Content-Disposition"] = f'attachment; filename="{
                stream.title}"'

            return response

        return JsonResponse({"response": "Error!", "date": datetime.datetime.now(), "user": "Generic", "errors": video_request_serializer.errors})
