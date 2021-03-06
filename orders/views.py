from django.shortcuts import render
from .models import OrderBook
from .forms import OrderCreateForm
from cart.cart import Cart
import random
from django.conf import settings
from django.contrib.auth.models import User


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderBook.objects.create(order=order,
                                         book=item['book'],
                                         quantity=item['quantity'],
                                         )

            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

