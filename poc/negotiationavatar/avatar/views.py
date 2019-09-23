from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile, Purpose
from django.contrib.auth import login



def home_page(request):
    userprofile = UserProfile.objects.all()
    print(userprofile)
    purpose = Purpose()
    return render(request, 'avatar/avatar_home.html', {'userprofile': userprofile, 'purpose': purpose})


def deals(request):
    return render(request, 'avatar/deals.html')


def registration_form(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('avatar:home')
    else:
        form = UserCreationForm()
    return render(request, 'avatar/register.html', {'form': form})


def login_form(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request, user)
            return redirect('avatar:home')

    else:
        form = AuthenticationForm()
    return render(request, 'avatar/login.html', {'form':form})
