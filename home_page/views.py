from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
        return render(request, 'index.html')

# def send(request):
#         res = request.POST["ans"]
#         return render(request, 'test.html' , {'answer':res})
