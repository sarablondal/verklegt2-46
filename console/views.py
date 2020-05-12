from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
import json
import datetime
import cart
from cart.models import *
import console
from console.forms.consoleForm import ConsoleCreateForm, ConsoleUpdateForm
from console.models import Console

# Create your views here.
def consoleIndex(request):
    if 'searchFilter' in request.GET:
        searchFilter = request.GET['searchFilter']
        consoles = [{
            'id': i.id,
            'name': i.name,
            'description': i.description,
            'company': i.company,
            'price': i.price,
            'firstImage': i.consoleimage_set.first().image
        } for i in Console.objects.filter(name__icontains=searchFilter)]

        return JsonResponse({'data': consoles})
    context = {'consoles': Console.objects.all()}  #order_by('name')
    return render(request, 'catalog/consoleIndex.html', context)

###########################################
def sortNameIndex(request):
    context = {'consoles': Console.objects.all().order_by('name')}  # order_by('name')
    return render(request, 'catalog/consoleIndex.html', context)

def sortPriceIndex(request):
    context = {'consoles': Console.objects.all().order_by('price')}  # order_by('price')
    return render(request, 'catalog/consoleIndex.html', context)
###########################################

# sækir gögn fyrir tiltekið console url, t.d. localhost:3000/consoles/3
def getConsoleById(request, id):
    return render(request, 'catalog/consoleDetails.html', {
        'console': get_object_or_404(Console, pk=id)
    })


def createConsole(request):
    if request.method == 'POST':
        print(1)
    else:
        form = ConsoleCreateForm()
    return render(request, 'catalog/createConsole.html', {
        'form': form
    })

def deleteConsole(request, id):
    console = get_object_or_404(Console, pk=id)
    console.delete()
    return redirect("consoleIndex")


def updateConsole(request, id):
    instance = get_object_or_404(Console, pk=id)
    if request.method == 'POST':
        form = ConsoleUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('consoleDetails', id=id)

    else:
        form = ConsoleUpdateForm(instance=instance)
    return render(request, 'catalog/updateConsole.html', {
        'form': form,
        'id': id
    })

#Sara gera order ddót

def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkoutuserinfo.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

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
        print('User is not logged in')

        print('COOKIES:', request.COOKIES)
        name = data['form']['name']
        email = data['form']['email']

        cookieData = cookieCart(request)
        items = cookieData['items']

        customer, created = Customer.objects.get_or_create(
            email=email,
        )
        customer.name = name
        customer.save()

        order = Order.objects.create(
            customer=customer,
            complete=False,
        )

        for item in items:
            product = Product.objects.get(id=item['id'])
            orderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity'],
            )

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)

#utils

def cookieCart(request):
    # Create empty store for now for non-logged in user
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        print('CART:', cart)

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']

    for i in cart:
        # We use try block to prevent items in store that may have been removed from causing error
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'id': product.id,
                'product': {'id': product.id, 'name': product.name, 'price': product.price,
                            'imageURL': product.imageURL}, 'quantity': cart[i]['quantity'],
                'digital': product.digital, 'get_total': total,
            }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass

    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(request, data):
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity'],
        )
    return customer, order
