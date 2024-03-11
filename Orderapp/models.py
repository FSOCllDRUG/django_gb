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


class OrderModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel, related_name='products')
    summa = models.DecimalField(decimal_places=2, default=0, max_digits=20)
    order_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Сначала сохраняем без вычисления суммы
        super().save(*args, **kwargs)
        # Затем вычисляем и обновляем сумму
        self.summa = sum(product.price for product in self.products.all())
        super().save(update_fields=['summa'])

    def __str__(self):
        return f'Order {self.id} with {self.products.count()} products'
