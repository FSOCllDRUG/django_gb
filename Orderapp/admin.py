from django.contrib import admin
from . import models

admin.site.register(models.ClientModel)
admin.site.register(models.ProductModel)
admin.site.register(models.OrderModel)
