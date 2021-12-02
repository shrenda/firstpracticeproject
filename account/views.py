from django.shortcuts import redirect, render, resolve_url

import account
from .models import Account,post
from django.contrib.auth.models import auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        passwrod2 = request.POST['password2']
        if password1 == passwrod2:
            if Account.objects.filter(username=username).exists():
                print('username taken')
                return redirect('register')
            elif Account.objects.filter(email=email).exists():
                print('email taken')
                return redirect('register')
            else:
                user = Account.objects.create_user(username=username, password=password1, email=email, name = name)
                user.save();

                return redirect('login')
        else:
            print('registered')
            return redirect('register')
    else:    
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user= auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('Invalid')
            return redirect('login')
    else:
        return render(request, "login.html")

def home(request):
    obj1 = post.objects.all()
    return render(request, "home.html", {'obj1':obj1})

def logout(request):
    auth.logout(request)
    return redirect('login')

def profile(request):

    obj = post.objects.filter(user__id = request.user.id)
    return render(request, "profile.html", {'obj':obj})