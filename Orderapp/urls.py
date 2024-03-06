from django.urls import path

from .views import client_orders_content, client_orders_for_period, product_form, show_product

urlpatterns = [
    path('client_orders_content/<int:client_id>/', client_orders_content, name='client_orders_content'),
    path('client_orders_for_period/<int:client_id>/<slug:period>', client_orders_for_period,
         name='client_orders_for_period'),
    path('add_product/', product_form, name='product_form'),
    path('show_product/<int:product_id>/', show_product, name='show_product'),
]
