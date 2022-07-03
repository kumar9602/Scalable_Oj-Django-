from django.db import models

# Create your models here.

class Problem(models.Model):
    name = models.CharField(max_length=200)
    problem_statement = models.CharField(max_length= 4000)
    code = models.CharField(max_length=4000)
    
    def _str_(self):
        return self.name
    
class Solution(models.Model):
    problem = models.ForeignKey(Problem , on_delete=models.CASCADE)
    verdict = models.CharField(max_length=50)
    submitted =models.DateTimeField()
    submitted_code = models.CharField(max_length=5000)
    
    def _str_(self):
        return self.verdict
class Testcases(models.Model):
    input = models.CharField(max_length=255)
    output = models.CharField(max_length= 255)
    problem = models.ForeignKey(Problem , on_delete=models.CASCADE)
    def _str_(self):
        return self.input
    
