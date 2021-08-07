from django.shortcuts import render,redirect
from .models import OrderItem,Order
from .forms import OrderCreateForm
from django.db.models import F
from django.conf import settings
from cart.cart import Cart
from shop.models import Product
from accounts.models import Account

def order_create(request):
    if not request.user.is_authenticated:
        return redirect('login')   
    else:
     cart = Cart(request)
    if request.method == 'POST':
        data = {'usid': request.user}
        form = OrderCreateForm(request.POST or None, initial=data)
        if form.is_valid():
            order = form.save(commit=False)
            form.usid= data
            order =form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                    )
                old = Product.objects.filter(name__iexact=item['product'])
                old.update(stock=F('stock') - item['quantity'])

            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        delivery = Account.objects.filter(phone__iexact=request.user)
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form ,'delivery':delivery})