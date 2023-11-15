from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def williumson(request):
    return HttpResponse('<h1>williumson betterluck next time</h1>')

def rachinravindra(request):
    return render(request,'rachin.html')