from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def education(request):
    return render(request, 'education.html')

def work(request):
    return render(request, 'work.html')

def research(request):
    return render(request, 'research.html')

def certifications(request):
    return render(request, 'certifications.html')
