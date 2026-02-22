from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer
from stores.models import Store
from services.twitter_service import post_tweet, upload_media


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_product(request, store_id):
    """
    Create a new product for a specific store and announce it via tweet.

    This view accepts POST data, validates it using the ProductSerializer,
    and creates a new Product instance associated with the given store.
    If the store does not exist, a 404 response is returned.

    After saving the product, the function constructs a tweet containing
    the product name, description, and the store it belongs to. If an image
    is provided, it is uploaded and attached to the tweet.

    Parameters:
        request (HttpRequest): The incoming request containing product data.
        store_id (int): The ID of the store the product belongs to.

    Returns:
        Response: A JSON representation of the created product with a 201 status,
                  or validation errors with a 400 status.
    """
    try:
        store = Store.objects.get(id=store_id)
    except Store.DoesNotExist:
        return Response({"detail": "Store not found."}, status=status.HTTP_404_NOT_FOUND)

    data = request.data.copy()
    data["store"] = store.id

    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        product = serializer.save()

        tweet_text = (
            f"New product added to {store.name}!\n"
            f"{product.name}: {product.description}"
        )

        media_id = None
        if product.image:
            media_id = upload_media(product.image.path)

        post_tweet(tweet_text, media_id)

        return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_store_products(request, store_id):
    """
    Retrieve and return all products belonging to a specific store.

    This view filters Product instances by the provided store_id,
    serializes the results, and returns them as a list. It does not
    require authentication and is intended for general browsing of
    products within a store.

    Parameters:
        request (HttpRequest): The incoming request.
        store_id (int): The ID of the store whose products are requested.

    Returns:
        Response: A JSON list of all products for the specified store.
    """
    products = Product.objects.filter(store_id=store_id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
