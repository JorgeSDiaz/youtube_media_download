from django.shortcuts import render
from django.http import JsonResponse
import datetime

# Create your views here.


def check(request):
    return JsonResponse({"response": "OK!", "date": datetime.datetime.now(), "user": "Generic"})
