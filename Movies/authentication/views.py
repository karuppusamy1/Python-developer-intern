from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken. Please choose a different one.")

        user = User.objects.create_user(username=username, email=email, password=password)

        login(request, user)
        return redirect('login')

    else:
        return render(request, "authentication/register.html")
def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('movies:index')
        else:
            return HttpResponse("wrong username or password")


    else:
        return render(request, "authentication/login.html")

def logout_view(request):
    logout(request)
    return HttpResponse("logged out successfully")