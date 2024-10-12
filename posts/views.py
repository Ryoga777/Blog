from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def post_singolo(request):
    return render(request, 'post_singolo.html')

def contatti(request):
    return render(request, 'contatti.html')

def chi_sono(request):
    return render(request, 'chi-sono.html')