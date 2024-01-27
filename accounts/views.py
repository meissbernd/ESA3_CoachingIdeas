from django.shortcuts import render
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def user_signup(request):
    """Handles user sign-up logic."""
    if request.method == 'GET':
        return render(request, 'signup.html',
                      {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html',
                              {'form': UserCreateForm,
                               'error': 'Benutzername bereits vergeben. Bitte einen neuen Benutzernamen wählen.'})
        else:
            return render(request, 'signup.html',
                          {'form': UserCreateForm, 'error': 'Passwörter stimmen nicht überein'})


@login_required
def user_logout(request):
    """Logs out the authenticated user."""
    logout(request)
    return redirect('home')


def user_login(request):
    """Handles user login logic."""
    if request.method == 'GET':
        return render(request, 'login.html',
                      {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'login.html',
                          {'form': AuthenticationForm(),
                           'error': 'Username und Passwort stimmen nicht überein'})
        else:
            login(request, user)
            return redirect('home')
