from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse("<H1>Hello World<H1>")
