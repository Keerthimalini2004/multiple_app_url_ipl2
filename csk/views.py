from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1>Rutu is captain of CSK</h1>')

def vice_captain(request):
    return HttpResponse('<h1>Dhoni is vice captain of CSK</h1>')
