from django.contrib import admin
from django.urls import path
from judge import views
app_name = 'judge'
urlpatterns = [
    path('' , views.problems  , name = 'problems'),
    path('about/' , views.about , name = 'about'),
    path('contact/' , views.contact , name = 'contact'),
    path('leaderboard/' , views.leaderboard , name = 'leaderboard'),
    path('details/' , views.details , name = 'details')
]