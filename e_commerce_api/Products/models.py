from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# def upload_to(instance, filename):
#     return 'images/{filename}'.format(filename=filename)

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField(models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)]
    ), default=1)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', null=True)
    #models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.name