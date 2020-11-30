from django.contrib import messages
from django.contrib.auth.models import User,auth
import psycopg2
from django.shortcuts import render, redirect

from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from accounts.security import BusinessUserBackend

import accounts.migrations

# function for testing
def EqualPassword(pass1,pass2):
    return pass1==pass2
def UserIsExists(username):
    return User.objects.filter(username=username).exists()
def EmailIsExists(email):
    return User.objects.filter(email=email).exists()


def custmer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if EqualPassword(password1,password2):
            if UserIsExists(username):
                messages.info(request, 'UserName Taken')
                return redirect('/accounts/custmer')
            elif EmailIsExists(email):
                messages.info(request, 'Email taken')
                return redirect('/accounts/custmer')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request, 'User Created')
                return redirect('/accounts/login')

        else:
            messages.info(request, 'password not matching..')
            return redirect('/accounts/custmer')
        return redirect('/home')

    else:
        return render(request, 'custmer.html')

def Business(request):

    if request.method == 'POST':

        username = request.POST['username']
        NameBusiness = request.POST['NameBusiness']
        Category = request.POST['Category']
        addres=request.POST['addres']
        Phone=request.POST['Phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if EqualPassword(password1,password2):
            if UserIsExists(username):
                messages.info(request, 'UserName Taken')
                return redirect('/accounts/Business')
            elif EmailIsExists(email):
                messages.info(request, 'Email taken')
                return redirect('/accounts/Business')
            else:
                bo = BusinessOwner.objects.create(UserName=username, Password=password1, Email=email, Category=Category, addres=addres,Phone=Phone,NameBusiness=NameBusiness)
                bo.save()
                messages.info(request, 'Business Created')
                return redirect('/accounts/login')

        else:
            messages.info(request, 'password not matching..')
            return redirect('/accounts/Business')
        return redirect('/home')

    else:
        return render(request, 'Business.html')

def login(request):
    userResponse = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userResponse = auth.authenticate(username=username, password=password)

        if userResponse is not None:
            auth.login(request, userResponse)
            return redirect("/home")
        if userResponse is None:
            messages.info(request, 'invalid credentials')
            return redirect("/accounts/login")
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/home")