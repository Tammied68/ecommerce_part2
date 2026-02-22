from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    """
    Represents a vendor-owned store within the application.

    Each store is associated with a specific user (vendor) and contains
    basic descriptive information such as a name, description, and an
    optional logo image. Stores serve as containers for related products.
    """

    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to="store_logos/", null=True, blank=True)

    def __str__(self):
        """
        Returns a readable string representation of the store.
        """
        return self.name


class Product(models.Model):
    """
    Represents a product belonging to a specific store.

    Products include a name, description, optional image, and optional price.
    When a new product is created through the Django admin, a tweet is
    automatically triggered to announce the addition (handled in admin.py).
    """

    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="product_images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        """
        Returns a readable string representation of the product.
        """
        return self.name
