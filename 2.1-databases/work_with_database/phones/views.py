from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phone_object = Phone.objects.all()
    sort_pages = request.GET.get('sort')
    if sort_pages == 'min_price':
        phone_object = phone_object.order_by('price')
    elif sort_pages == 'max_price':
        phone_object = phone_object.order_by('-price')
    elif sort_pages == 'name':
        phone_object = phone_object.order_by('name')
    template = 'catalog.html'
    context = {'phones': phone_object}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {'phone': phone[0]}
    return render(request, template, context)
