from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
from .models import feedbackBox
from .form import create_feedback
from django.http import HttpResponse
from account.models import Business

def feedback(request):
    form = create_feedback()
    if request.method == 'POST':
        form = create_feedback(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'feedback.html', context)


def home(request):
    shops = Business.objects.all()
    return render(request, 'index.html',{'shops':shops})


def Abutus(request):
    return render(request, 'abutUs.html')


def Registar(request):
    return render(request, 'Registar.html')

# def AddProduct(request):
#         return render(request,'AddProduct.html')
