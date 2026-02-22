from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stores")
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to="store_logos/", null=True, blank=True)

    def __str__(self):
        return self.name
