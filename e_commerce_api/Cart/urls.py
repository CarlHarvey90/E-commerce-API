from django.urls import path
from . import views
#from api.views import products

app_name = 'cart'

urlpatterns = [
    #path('/', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('products/', views.product_list, name='products'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]