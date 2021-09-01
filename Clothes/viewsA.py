from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .decorators import *

# @unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account was created successfully" + form.cleaned_data.get('username'))
            return redirect('login')

    return render(request, "Accounts/register.html", {
        "Form" : form
    })

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('userpage')
        else:
            messages.info(request, "Username or Password is incorrect")

    return render(request, 'Accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')