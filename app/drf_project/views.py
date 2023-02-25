# app/drf_project/views.py

from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong 123"}
    return JsonResponse(data)
