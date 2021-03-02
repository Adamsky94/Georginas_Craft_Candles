from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    scent =  models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promotion = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
