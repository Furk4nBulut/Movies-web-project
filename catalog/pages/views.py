from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#http://127.0.0.1:8000/

def travelwebpage(request):
    return render(request, 'pages/travelwebpage.html')

def blog(request):
    return render(request, 'pages/blog.html')