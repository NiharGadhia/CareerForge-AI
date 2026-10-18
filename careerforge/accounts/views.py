from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import RegisterForm
from userprofile.models import UserProfile
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)

            # Check if user already has a profile
            if UserProfile.objects.filter(user=user).exists():
                return redirect('dashboard')

            # New user → profile
            return redirect('profile')

        messages.error(request, 'Invalid username or password.')
        return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')