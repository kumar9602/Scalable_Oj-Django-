from django.http import HttpResponse
from django.shortcuts import render 

# Create your views here.
def problems(request):
    return render(request , 'index.html')
def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html' )
