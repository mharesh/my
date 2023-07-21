from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cricket(request):
    return HttpResponse('we will play cricket on saturday or sunday')

def movie(request):
    return HttpResponse('we are going to movie on sunday')