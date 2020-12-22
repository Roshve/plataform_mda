from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def pages_home(request):
    
    return render(request, 'index.html')

def form_news_users(request):

    return render(request, 'form/form_news_users.html')