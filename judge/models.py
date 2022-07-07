from doctest import testfile
from sqlite3 import Timestamp
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Problem(models.Model):
    Difficulty_choices = (
        ('hard' , 'hard'),
        ('medium'  ,'medium'),
        ('easy' , 'easy'),
    )
    name = models.CharField(max_length=200)
    problem_statement = models.TextField()
    problem_difficulty = models.CharField(max_length= 15 , choices= Difficulty_choices , default='easy')
    
    def _str_(self):
        return self.name
    
class Solution(models.Model):
    language_choices = (
        ('c++' , 'cpp'),
    )
    verdict_choices = (
        ('PS' , 'processing'),
        ('WA' , 'wrong answer'),
        ('AC' , 'accepted'),
        ('TLE' , 'time limit excedded'),
        ('MLE' , 'memory limit excedded'),
    )
    problem = models.ForeignKey(Problem , on_delete=models.CASCADE)
    language = models.CharField(max_length= 10 ,choices = language_choices)
    verdict = models.CharField(max_length=10 , choices= verdict_choices)
    code_file = models.FileField(upload_to='code_file/' , null=False)
    Timestamp = models.TimeField(auto_now_add = True )
    
    
class Testcases(models.Model):
    problem = models.ForeignKey(Problem , on_delete=models.CASCADE)
    test_input = models.FileField(upload_to = 'test_inputs/' , null= False)
    test_output = models.FileField(upload_to = 'test_outputs' , null = False)
    
