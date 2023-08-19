from django.shortcuts import render

# Create your views here.

def index(request , *args, **kwargs):
    #allows us to render index.html
    return render(request, 'frontend/index.html')