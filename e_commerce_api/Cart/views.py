from django.shortcuts import render, redirect
from .models import Products, CartItem
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user_model

# def product_list(request):
#     products = Products.objects.all()
#     return render(request, 'myapp/index.html', {'products': products})

#User = get_user_model()
@login_required
def view_cart(request):
    #users = Users.objects.all()
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

