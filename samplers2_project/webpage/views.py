from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def home(request):
    return render(request, 'webpage/home.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

