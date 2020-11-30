from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
        return render(request, 'index.html')

def Abutus(request):
        return render(request, 'abutUs.html')

def Registar(request):
        return render(request,'Registar.html')


# def send(request):
#         res = request.POST["ans"]
#         return render(request, 'test.html' , {'answer':res})
