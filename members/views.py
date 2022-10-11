from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from event.models import Msg
from event.forms import MsgForm

# Create your views here.


def chat(request):
    user = request.user
    msgs = Msg.objects.all().order_by('id')
    if request.method == 'POST':
        
        form = MsgForm(request.POST)
        form.save()
        
        redirect('home')
    else:
        text = ''
    return render(request, 'chat.html', {'text':request.POST, 'user':user, 'msgs':msgs})


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