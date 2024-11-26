from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>kholi is captain of rcb</h1>')


def quotes(request):
    return HttpResponse('<h1>eeshala cup namadhey</h1>')