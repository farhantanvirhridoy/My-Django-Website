from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect('home')
    else:
            form = UserCreationForm()
    return render(request, 'register.html', {"form":form })



def logout_user(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully")
            return redirect('home')
            
            # Redirect to a success page
        else:
            messages.success(request, "There is an error when loggin in")
            return redirect('login_user')
    
    else:
        # Return an 'invalid login' error message.
        ...
        return render(request, 'login.html', {})