from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as loginUser, logout as logoutUser, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from ecommerce_website.helpers.helper import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm

def login(request):
    if request.method == 'POST':
        next_url = request.POST.get('next', '')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            loginUser(request, user)
            messages.success(request, 'Login successfully!')
            if next_url:
                return redirect(next_url)
            return redirect('/')
        else:
            messages.error(request, form.errors.as_text())
            return redirect(f'/auth/login?next={next_url}')
    else:
        context = getDefault(request)
        if request.user.is_authenticated:
            return redirect('/user/profile')
        form  = AuthenticationForm()
        return render(request, 'auth/login.html', {'form':form, **context})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Password entered in the form
            user = User.objects.get(username=username)
            user.email  = request.POST.get('email')
            user.first_name  = request.POST.get('first_name')
            user.last_name  = request.POST.get('last_name')
            user.save()
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user:
                loginUser(request, authenticated_user)
            return redirect('profile')  # Redirect to login page after registration
        else:
            messages.error(request, form.errors.as_text())
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html')


@login_required(login_url="/auth/login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
            print('success')
            messages.success(request, 'Password changed Successfully')
            return redirect('/auth/change-password')
        else:
            print('some error')
            print(form.errors)
            messages.error(request, form.errors.as_text())
            return redirect('/auth/change-password')
    else:
        context = getDefault(request)
        userprofile = getAccount(request)
        form  = PasswordChangeForm(request.user)
        return render(request, 'user/change_password.html', {**context, 'profile':userprofile, 'form': form})


@login_required(login_url="/auth/login")
def logout(request):
    logoutUser(request)
    return redirect('/')
 