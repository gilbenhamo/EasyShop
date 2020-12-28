from django.shortcuts import render
from django.urls import reverse
from .models import comments
from account.models import Business, Customer
from review.form import RateForm
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect


def commentt(request,busi_id):
    business = Business.objects.get(user_id=busi_id)
    revs = comments.objects.all()
    sum =0
    count =0
    avg=0
    for r in revs:
        if r.business_comments_id == business.user_id:
            sum += r.rate
            count+=1
    if count != 0:
        avg=float('%.2f'%(sum/count))


    user = request.user
    form =RateForm()
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.business_comments = business
            comment.save()
        return redirect('/review/{0}/'.format(business.user_id))
    context = {'reviews': form,'revs':revs,'busin':business,'avgrate':avg}
    return render(request, 'reviews.html', context)
