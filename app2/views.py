from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course(request):
    return HttpResponse('today attend aptitude class')

def course1(request):
    return HttpResponse('<marquee><h1>present class on going</h1></marquee>')