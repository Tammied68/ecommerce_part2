from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Store
from .serializers import StoreSerializer
from services.twitter_service import post_tweet, upload_media


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_store(request):
    """
    Create a new store for the authenticated vendor and announce it via tweet.

    This view accepts POST data, validates it using the StoreSerializer,
    and creates a new Store instance associated with the authenticated user.
    After saving the store, the function constructs a tweet containing the
    store's name and description. If a logo image is provided, it is uploaded
    and attached to the tweet.

    Parameters:
        request (HttpRequest): The incoming request containing store data.

    Returns:
        Response: A JSON representation of the created store with a 201 status,
                  or validation errors with a 400 status.
    """
    serializer = StoreSerializer(data=request.data)
    if serializer.is_valid():
        store = serializer.save(vendor=request.user)

        tweet_text = f"New store added: {store.name}\n{store.description}"

        media_id = None
        if store.logo:
            media_id = upload_media(store.logo.path)

        post_tweet(tweet_text, media_id)

        return Response(StoreSerializer(store).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_stores(request):
    """
    Retrieve and return a list of all stores.

    This view fetches all Store instances from the database, serializes them,
    and returns the full list. It does not require authentication and is
    intended for public or general browsing of available stores.

    Parameters:
        request (HttpRequest): The incoming request.

    Returns:
        Response: A JSON list of all stores.
    """
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)
