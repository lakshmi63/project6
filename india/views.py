from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse('<h1> this is virat s 50 th century</h1>')

def shami(request):
    return render(request,'ssh.html')