from django.shortcuts import render,redirect
from .models import product
from .form import createProduct
from django.views.generic import CreateView

# Create your views here.
def create_product(request):
    form = createProduct()
    if request.method == 'POST':
        form = createProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'AddProduct.html', context)
