from django.core.management.base import BaseCommand

from Orderapp.models import ProductModel


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = ProductModel(name='carrot', description='yellow', price=1.99, amount=1, add_date='2024-01-02')
        product.save()
        self.stdout.write(f'{product} added')

        product = ProductModel(name='tomato', description='black', price=5.99, amount=1, add_date='2024-01-02')
        product.save()
        self.stdout.write(f'{product} added')

        product = ProductModel(name='pineapple', description='juicy', price=14.99, amount=1, add_date='2024-01-02')
        product.save()
        self.stdout.write(f'{product} added')

        product = ProductModel(name='apple', description='green', price=3.99, amount=4, add_date='2024-01-02')
        product.save()
        self.stdout.write(f'{product} added')

        product = ProductModel(name='meat', description='beef', price=10.99, amount=1, add_date='2024-01-02')
        product.save()
        self.stdout.write(f'{product} added')

        product = ProductModel(name='fish', description='clown', price=18.99, amount=1, add_date='2024-01-02')
        product.save()
        self.stdout.write(f'{product} added')
