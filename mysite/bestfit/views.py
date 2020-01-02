from django.shortcuts import render
from .models import Test

def profile(request):
    return render(request, 'profile.html')


def index(request):
    return render(request, 'index.html')


def profileEdit(request):
    return render(request, 'profileEdit.html')


def instructions(request):
    return render(request, 'instructions.html')


def sample_test(request):
    questions = Test.objects.all()
    return render(request, 'sampleTest.html',{"questions": questions})


def feedback(request):
    return render(request, 'feedback.html')


def lockscreen(request):
    return render(request, 'lockScreern.html')


def register(request):
    return render(request, 'register.html')


