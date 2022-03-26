from django.http import HttpResponse
from django.shortcuts import render
from django . http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def fun(request):
    return render(request,'home.html',{'name':'Arun'})
def webp(request):
    return render(request,'home1.html')