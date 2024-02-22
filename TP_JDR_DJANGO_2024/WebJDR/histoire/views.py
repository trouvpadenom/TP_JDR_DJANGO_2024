from django.shortcuts import render
from django.urls import reverse

def mort(request):
    return render(request, 'mort.html')

def victoire(request):
    return render(request, 'victoire.html')

def chap1(request):
    return render(request, 'chap1.html')

def chap2(request):
    return render(request, 'chap2.html')

def chap3(request):
    return render(request, 'chap3.html')

