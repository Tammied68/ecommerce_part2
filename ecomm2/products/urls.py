from django.urls import path
from . import views

"""
URL configuration for the Products API.

This module defines the URL routes for listing products belonging
to a specific store and for adding new products to that store.
These endpoints are used by the Django REST Framework views in
products/views.py.
"""

urlpatterns = [
    path(
        "stores/<int:store_id>/products/",
        views.list_store_products,
        name="list_store_products",
    ),
    path(
        "stores/<int:store_id>/products/add/",
        views.add_product,
        name="add_product",
    ),
]
