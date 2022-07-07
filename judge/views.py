from django.contrib.auth import login
from django.contrib import messages
from distutils.command.upload import upload
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render ,redirect
import subprocess
import filecmp
from judge.models import Problem, Solution, Testcases
from django.core.files import File

# Create your views here.
def problems(request):
    problems = Problem.objects.all()
    return render(request , 'index.html' , { 'index' : problems})
def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html' )
def leaderboard(request):
    return render(request , 'leaderboard.html')
def details(request):
    return render(request , 'details.html')
