from django.urls import path
from . import views

"""
URL configuration for the Stores API.

This module defines the URL routes for listing stores and creating
new store instances. These endpoints are used by the Django REST
Framework views in stores/views.py.
"""

urlpatterns = [
    path("stores/", views.list_stores, name="list_stores"),
    path("stores/create/", views.create_store, name="create_store"),
]
