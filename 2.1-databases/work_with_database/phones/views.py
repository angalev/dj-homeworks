from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):

    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sorting = request.GET.get('sort')

    if sorting == 'name':
        phones = Phone.objects.all().order_by('name')
    if sorting == 'min_price':
        phones = Phone.objects.all().order_by('price')
    if sorting == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    if not sorting:
        phones = Phone.objects.all()

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
