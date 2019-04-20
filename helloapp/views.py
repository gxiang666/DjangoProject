from django.shortcuts import render

# Create your views here.
# views.py中包含对某个HTTP请求(url)的响应
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello World! I am coming...")
