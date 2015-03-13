from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserCreationForm, ConnexionForm


def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
        messages.success(request, 'You have been logged out successfully !')

    return redirect('index', permanent=True)


def user_add(request):
    error = False

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            messages.success(request, 'Account created. You can now log in.')
            return render(request, 'global/index.html', locals())
    else:
        form = UserCreationForm()

    return render(request, 'users/user_add.html', locals())


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Welcome %s. You are now logged in =)' % user.username)
        else:
            messages.error(request, 'Authentication failed with this username and password.')
            return redirect('connexion_view')

    return redirect('index')


def connexion_view(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Welcome %s. You are now logged in =)' % user.username)
            else:
                messages.error(request, 'Authentication failed with this username and password.')
                return redirect('connexion_view')

    else:
        form = ConnexionForm()

    return render(request, 'users/connexion.html', locals())