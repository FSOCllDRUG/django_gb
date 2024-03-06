import datetime

from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
from .models import ClientModel, OrderModel, ProductModel


def client_orders_content(request, client_id):
    client = get_object_or_404(ClientModel, pk=client_id)
    orders = OrderModel.objects.filter(client=client)

    context = {'client': client, 'orders': orders}
    return render(request, 'Orderapp/client_orders_content.html', context)


def client_orders_for_period(request, client_id, period):
    client = get_object_or_404(ClientModel, pk=client_id)
    orders = OrderModel.objects.filter(client_id=client_id).order_by('order_date')
    products_for_period = set()
    today = datetime.date.today()
    for order in orders:
        delta_time = (today - order.order_date).days
        if period == 'week':
            if delta_time <= 7:
                for product in order.products.all():
                    products_for_period.add(product)
        if period == 'month':
            if delta_time <= 30:
                for product in order.products.all():
                    products_for_period.add(product)
        if period == 'year':
            if delta_time <= 365:
                for product in order.products.all():
                    products_for_period.add(product)
    context = {'client': client, 'period': period, 'product_list': products_for_period}
    return render(request, 'Orderapp/client_orders_for_period.html', context)


def show_product(request, product_id):
    product = get_object_or_404(ProductModel, pk=product_id)
    return render(request, 'Orderapp/product.html', {'product': product})


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            saved_form = form.save()
            return render(request, 'Orderapp/product_form.html', {'form': form, 'saved_form': saved_form})
        else:
            form = ProductForm()
    else:
        form = ProductForm()
    return render(request, 'Orderapp/product_form.html', {'form': form})
