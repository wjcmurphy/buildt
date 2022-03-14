from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from accounts.forms import CreateUserForm

# Create your views here.


def login(request):
    return render(request, 'accounts/login.html')


def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == "GET":
        return render(request, "accounts/signup.html", {"form": CreateUserForm})
    elif request.method == "POST":
        form = CreateUserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return render(request, "accounts/profile.html")
        else:
            return render(request, "accounts/signup.html", {'form': form})