from random import choice, randint

from django.core.management.base import BaseCommand

from Orderapp.models import OrderModel, ProductModel, ClientModel


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        client_name = choice(['John', 'Emily', 'Robert'])
        client = ClientModel.objects.get(name=client_name)
        all_products = ['pineapple', 'apple', 'fish', 'meat', 'carrot', 'tomato']

        order_products = list()
        rand_order_amount = randint(1, 6)

        for i in range(rand_order_amount):
            product_name = choice(all_products)
            order_products.append(ProductModel.objects.get(name=product_name))
            all_products.remove(product_name)

        summa = 0
        for product in order_products:
            summa += product.amount * product.price

        order = OrderModel(client=client, summa=summa)

        order.save()
        order.products.set(order_products)
        order.save()
        self.stdout.write(f'{order} added')
