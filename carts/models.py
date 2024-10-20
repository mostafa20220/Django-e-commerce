from django.core.validators import MinValueValidator
from django.db import models
from products.models import ProductVariant
from users.models import User




class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,related_name='cart')
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, editable=False,related_name='cart')
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    # don't allow duplicate product_variant for the same customer instead update the quantity
    class Meta:
        unique_together = ['customer', 'product_variant']
