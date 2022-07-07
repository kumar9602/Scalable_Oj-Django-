from django.contrib import admin
from .models import Problem
from .models import Solution
from .models import Testcases
# Register your models here.
admin.site.register(Problem) ,
admin.site.register(Solution) ,
admin.site.register(Testcases)