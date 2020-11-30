from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.models import BusinessOwner,user
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

        else:
            messages.info(request, 'password not matching..')
            return redirect('/accounts/Business')
        return redirect('/home')

    else:
        return render(request, 'Business.html')











    # if request.method == 'POST':
    #     UserName = request.POST['UserName']
    #     Password = request.POST['Password']
    #     password2 = request.POST['Password2']
    #     RegisterDate = [12/11/1994]
    #     Email = request.POST['Email']
    #     Name = request.POST['Name']
    #     addres = request.POST['addres']
    #     Phone = request.POST['Phone']
    #     Age = request.POST['Age']
    #     # if Password==password2:
    #     #     if custmer.object.filter(UserName==UserName).exists():
    #     #         print("User Name Taken")
    #
    #     custmer1 = User.objects.create_user(UserName=UserName, Password=Password,Email=Email,RegisterDate=RegisterDate, Name=Name, addres=addres, Phone=Phone, Age=Age)
    #     custmer1.save()
    #     print("User Created")
    #     return redirect('/')
    # # first_name=request.POST['first_name']
    # # user=User.objects

# def registerCustmer(request):
#     if request.method == 'POST':
#         UserName = request.POST['UserName']
#         Password = request.POST['Password']
#         password2 = request.POST['Password2']
#         RegisterDate = request.POST['RegisterDate']
#         Email = request.POST['Email']
#         Name = request.POST['Name']
#         addres = request.POST['addres']
#         Phone = request.POST['Phone']
#         Age = request.POST['Age']
#         # if Password==password2:
#         #     if custmer.object.filter(UserName==UserName).exists():
#         #         print("User Name Taken")
#
#         user = User.object.create_user(UserName=UserName, Password=Password, RegisterDate=RegisterDate,
#                                                 Email=Email, Name=Name, addres=addres, Phone=Phone, Age=Age)
#         user.save()
#         print("User Created")
#         return redirect('/')
