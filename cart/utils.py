import json

from console.models import ConsoleImage
from .models import *

import console
from console.views import *

def cookieCart(request):
    # Create empty cart for now for non-logged in user
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        print('CART:', cart)

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']

    for i in cart:
        # We use try block to prevent items in cart that may have been removed from causing error
        try:
            cartItems += cart[i]['quantity']

            product = Console.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'id': product.id,
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL
                },
                'quantity': cart[i]['quantity'],
                'digital': product.digital,
                'get_total': total,
            }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass

    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
    cart = json.loads(request.COOKIES['cart'])
    itemquantity = []
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']

    for i in cart:
        if i == '':
            continue

        cartItems += cart[i]['quantity']
        console = Console.objects.filter(pk=int(i)).first()
        image = ConsoleImage.objects.filter(pk=int(i)).first()
        total = (console.price * cart[i]['quantity'])
        order['get_cart_total'] += total
        order['get_cart_items'] += cart[i]['quantity']
        item = {
            'id': console.id, 'name': console.name, 'price': console.price,
            'imageURL': image.image, 'quantity': cart[i]['quantity'], 'get_total': total,
        }
        items.append(item)
        itemquantity.append(cart[i]['quantity'])

   # context = {'items': items, 'order': order, 'cartItems': cartItems}

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
        product = Console.objects.get(id=item['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity'],
        )
    return customer, order