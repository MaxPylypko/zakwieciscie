from django.shortcuts import render
from django.http import HttpRequest
from catalog.models import *



# Create your views here.
def cart(request: HttpRequest):
    items_id = request.session.get('cart')
    try:
        cart_items = (Flower.objects.get(id=item_id) for item_id in items_id) 
    except:
        return render(request, 'order/cart.html')
    return render(request, "order/cart.html", {'cart_items': cart_items})