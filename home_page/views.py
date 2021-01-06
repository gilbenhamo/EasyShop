from django.shortcuts import render, redirect
from .form import create_feedback
from account.form import CATEGORY_BUSINESS
from account.models import Business, superMassage, Customer


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
    massage = superMassage.objects.all()
    return render(request, 'index.html', {'shops': shops, 'category': sorted(map(lambda x: x[1], CATEGORY_BUSINESS)),
                                          'categorIndex': map(lambda x: x[0], CATEGORY_BUSINESS),
                                          'massage': massage})  # sorted business categories


def Abutus(request):
    return render(request, 'abutUs.html')


def Registar(request):
    return render(request, 'Registar.html')


def searchByCategory(request, categ):
    shops = Business.objects.all()
    list = tuple(map(lambda x: x[1], CATEGORY_BUSINESS))  # Returns a list of all categories by name
    q = str(list.index(categ) + 1)  # Saves the ID of the desired category
    return render(request, 'serchByCategory.html', {'shops': shops, 'categ': q, 'categName': categ})


def search(request):
    shops = Business.objects.all()
    context = {}
    list = []
    if request.method == 'POST':
        name = request.POST.get('s')
        for shop in shops:
            if name in shop.business_name:  # Make a list of all the stores that have the word search
                list.append(shop)
        context = {'shops': shops, 'name': name, 'list': list}
    return render(request, 'search.html', context)


def adminReports(request):
    business = Business.objects.all()
    customer = Customer.objects.all()
    context = {'business': business, 'customer': customer}
    return render(request, 'admin_reports.html', context)


def guides(request):
    return render(request, 'guides.html')
