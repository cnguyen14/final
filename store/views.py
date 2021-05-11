from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cartData, guestOrder
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


def store(request):
    data = cartData(request)
    cItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)

    cItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)

    cItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)


def registerPage(request):
    context = {}
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Successfully Registered!!!' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'store/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.info(request, 'Username or Password is incorrect!!')
            return render(request, 'store/login.html')
    context = {}
    return render(request, 'store/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def orderlist(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'store/orderlist.html', context)


def orderdetail(request, pk_test):
    order = Order.objects.get(id=pk_test)
    orderItems = order.orderitem_set.all()
    shipping = order.shippingaddress_set.all()
    context = {'order': order, 'orderItems': orderItems, 'shipping': shipping}
    return render(request, 'store/orderdetail.html', context)
