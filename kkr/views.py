from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>the team kolkata</h1>')

def vice_captain(request):
    return HttpResponse('<h1>the vice captain is unknown</h1>')
