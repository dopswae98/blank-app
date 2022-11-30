from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, "EmploymentAgency/index.html", {"message": None})

def vaccancies(request):
    if not request.user.is_authenticated:
        return render(request, "EmploymentAgency/vaccancies.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "EmploymentAgency/user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username = username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("users:index"))
    else:
        return render(request, "users/login.html", {"message":"Invalid Credentials"})

def logout_view(request):
    logout(request)
    return render(request, "EmploymentAgency/login.html", {"message":"Logged Out."})

def jobs(request):
    logout(request)
    return render(request, "EmploymentAgency/jobs.html", {"message":"Logged Out."})

def aboutus(request):
    logout(request)
    return render(request, "EmploymentAgency/aboutus.html", {"message":None})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
           form.save() 
        
        #return redirect("users:user")
        return HttpResponseRedirect(reverse("users:user"))
        
    else:
        form = RegisterForm()
    
    return render(response, "EmploymentAgency/register.html", {"form":form})

def user(request):
    return HttpResponseRedirect(reverse("users:user"))