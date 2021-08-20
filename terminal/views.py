from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Terminal
import requests
# Create your views here.

 
@csrf_exempt
def index(request):
    return render(request, "index.html")


@csrf_exempt
def save(request):
    if request.method == 'POST':


        vulnerability = request.POST.get('vulnerability')
        ram = request.POST.get('ram')
        core = request.POST.get('core')

        print(vulnerability)

        return HttpResponse(vulnerability, ram, core)
    
