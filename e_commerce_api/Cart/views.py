from django.shortcuts import render, redirect
from .models import Products, CartItem
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user_model

def product_list(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'products': products})

#User = get_user_model()
@login_required
def view_cart(request):
    #users = Users.objects.all()
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')