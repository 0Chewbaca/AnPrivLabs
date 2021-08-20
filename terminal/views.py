from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Terminal
# Create your views here.

 
@csrf_exempt
def index(request):
    return render(request, "index.html")


@csrf_exempt
def save(request):
    if request.method == 'POST':

        vulnerability = request.POST['vulnerability']
        ram = request.POST['ram']
        core = request.POST['core']
        print(vulnerability)
        print(ram)
        print(core)

        return render(request, "index.html")
    
