from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from .models import User

def home(request):
    return redirect("login")

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            if user.role == "patient":
                return redirect("patient_dashboard")
            else:
                return redirect("doctor_dashboard")

        return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


@login_required
def patient_dashboard(request):
    if request.user.role != "patient":
        return redirect("login")
    return render(request, "patient_dashboard.html")


@login_required
def doctor_dashboard(request):
    if request.user.role != "doctor":
        return redirect("login")
    return render(request, "doctor_dashboard.html")


def logout_view(request):
    logout(request)
    return redirect("login")
