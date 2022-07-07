#from http.client import HTTPResponse  # if want to include a simple static page
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

## This is how to display a very simple static page
# def simple_page(request):
#  return HttpResponse('This is a Single Project Page')

urlpatterns = [
    # path('simple_page/', simple_page, name='simple_page'),  #this is how to display a very simple static page--call a function that returns a HttpResponse
    path('admin/', admin.site.urls), 
    path('', include('projects.urls')),
    path('polls/', include('polls.urls')),
]
