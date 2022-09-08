from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

# signup form 
def signup(request):
    return render(request, 'signupForm.html')

# login form 
def login(request):
    return render(request, 'loginForm.html')