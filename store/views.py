from django.contrib.auth.forms import UserCreationForm
from django.db.models import QuerySet
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import *
from .models import Product


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = OrderItem.objects.all()[0]

    context = {'items': items}
    return render(request, 'store/cart.html', context)


def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = OrderItem.objects.all()[0]

    context = {'items': items}

    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('adress', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zipcode', '')
        country = request.POST.get('country', '')
        print(name, email, country, city)
        customer = Customer(name=name, email=email)
        customer.save()
        shipping = ShippingAddress(customer=customer, address=address, city=city, state=state, zipcode=zipcode, country=country)
        shipping.save()

    return render(request, 'store/checkout.html', context)


def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product': product}
        template = 'store/single.html'
        return render(request, template, context)
    except:
        raise Http404

def contact(request):
    context = {}
    if request.method=="POST":
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname', '')
        country = request.POST.get('country', '')
        subject = request.POST.get('subject', '')
        print(firstname,lastname,country,subject)
        contact = Contact(firstname=firstname, lastname=lastname, country=country, subject=subject)
        contact.save()
        messages.success(request, "Wir haben ihre Nachricht empfangen. Wir werden uns bald bei Ihnen melden.")
        return redirect('contact')
    return render(request, 'store/contact.html', context)

def loginPage(request):
    context = {}
    return render (request, 'store/login.html', context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        customer = Customer(name=name, email=email, password1=password1, password2=password2)
        customer.save()
        messages.success(request, "Account wurde erstellt.")
        return redirect('login')

    context = {'form':form}
    return render (request, 'store/register.html', context)


def update_cart(request,slug):
    cart = OrderItem.objects.all()[0]
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    if not product in cart.products.all():
        cart.products.add(product)
        cart.quantity+=1
        cart.save()
    else:
        cart.products.remove(product)
        cart.quantity-=1
        cart.save()
    new_total = 0.00
    for item in cart.products.all():
        new_total += item.price
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse("cart"))
