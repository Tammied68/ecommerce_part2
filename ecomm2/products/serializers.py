from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product instances.

    This serializer handles validation and transformation of Product
    model data for API requests and responses. It exposes key fields
    such as name, description, image, and price, while ensuring that
    the product ID and associated store are read-only to prevent
    unauthorized reassignment through the API.
    """

    class Meta:
        model = Product
        fields = ["id", "store", "name", "description", "image", "price"]
        read_only_fields = ["id", "store"]
