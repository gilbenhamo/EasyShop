
from django.contrib import messages
from django.contrib.auth.models import User,auth
import psycopg2
from django.shortcuts import render, redirect
from .models import baseUser,baseUserManager ,Customer
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from accounts.security import BusinessUserBackend

import accounts.migrations

# function for testing
def EqualPassword(pass1,pass2):
    return pass1==pass2
# def UserIsExists(username):
#     return baseUser.objects.filter(email).exists()
def EmailIsExists(email):
    return baseUser.objects.filter(email=email).exists()
# Create your views here.
def custmer(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        #username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        phone = request.POST['phone']
        age = request.POST['age']
        if EqualPassword(password1,password2):
            # if UserIsExists(username):
            #     messages.info(request, 'UserName Taken')
            #     return redirect('/accounts/custmer')
            # if EmailIsExists(email):
            #     messages.info(request, 'Email taken')
            #     return redirect('/acc/custmer')
            # else:
                user = baseUser.object.create_customer(email=email, full_name=full_name, password=password1, address=address, phone=phone, age=age)
                user.save()
                messages.info(request, 'User Created')
                return redirect('/acc/login')

        else:
            messages.info(request, 'password not matching..')
            return redirect('/acc/custmer')
        return redirect('/home')

    else:
        return render(request, 'custmer.html')


def Business(request):

    if request.method == 'POST':

        #username = request.POST['username']
        full_name = request.POST['full_name']
        BusinessName = request.POST['BusinessName']
        Category = request.POST['Category']
        address=request.POST['address']
        phone=request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if EqualPassword(password1, password2):
            # if UserIsExists(username):
            #     messages.info(request, 'UserName Taken')
            #     return redirect('/accounts/custmer')
            # if EmailIsExists(email):
            #     messages.info(request, 'Email taken')
            #     return redirect('/acc/custmer')
            # else:
            user = baseUser.object.create_business(email=email, full_name=full_name, password=password1,
                                                   address=address, phone=phone, Category=Category, BusinessName=BusinessName)
            user.save()
            messages.info(request, 'User Created')
            return redirect('/acc/login')

        else:
            messages.info(request, 'password not matching..')
            return redirect('/acc/business')
        return redirect('/home')

    else:
        return render(request, 'Business.html')

def login(request):
    userResponse = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        userResponse = auth.authenticate(email=email, password=password)

        if userResponse is not None:
            auth.login(request, userResponse)
            return redirect("/home")
        if userResponse is None:
            messages.info(request, 'invalid credentials')
            return redirect("/acc/login")
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/home")