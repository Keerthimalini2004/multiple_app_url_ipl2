from django.urls import path

from kkr.views import*

urlpatterns=[
    path('captain/',captain,name='captain'),
    path('vice_captain/',vice_captain,name='vice_captain'),
   
]