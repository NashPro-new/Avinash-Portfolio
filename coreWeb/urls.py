from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   
    path('education', views.education, name='education'),  
    path('work', views.work, name='work'), 
    path('research', views.research, name='research'),  
    path('certifications', views.certifications, name='certifications'),
]