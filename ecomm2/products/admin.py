from django.contrib import admin
from .models import Product
from services.twitter_service import post_tweet


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Product model.
    Automatically triggers a tweet when a new product is created.
    """

    def save_model(self, request, obj, form, change):
        """
        Overrides the default save behavior in Django admin.

        When a new Product instance is created (not updated),
        this method triggers the post_tweet function to announce
        the new product. The method also prints a confirmation
        message to the terminal for debugging and verification.

        Parameters:
            request: The current HttpRequest object.
            obj: The Product instance being saved.
            form: The submitted form data.
            change: Boolean indicating whether this is an update (True)
                    or a new object creation (False).
        """
        print("SAVE MODEL OVERRIDE RAN")
        super().save_model(request, obj, form, change)

        if not change:
            message = f"New product added: {obj.name}"
            post_tweet(message)
