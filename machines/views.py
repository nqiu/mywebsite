from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'machines/index.html')

def signin(request):
    return render(request, 'machines/signin.html')

def signup(request):
    return render(request, 'machines/signup.html')

def setup(request):
    return render(request, 'machines/setup.html')

def progress(request):
    return render(request, 'machines/progress.html')


