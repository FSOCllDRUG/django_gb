from django.db import models


class ClientModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    reg_date = models.DateField()

    def __str__(self):
        return f'Client {self.name}'


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    amount = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return f'Product {self.name} for {self.price}'


def func():
    products = ProductModel.objects.all()
    summa = 0
    for product in products:
        summa += product.price * product.amount
    return summa


class OrderModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel, related_name='products')
    summa = models.DecimalField(decimal_places=2, default=func(), max_digits=20)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.products}'
