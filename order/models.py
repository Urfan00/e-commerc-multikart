from django.db import models
from products.models import ProductVersion
from django.contrib.auth import get_user_model
User = get_user_model()



class Wishlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_wishlist")
    product_version_id = models.ManyToManyField(ProductVersion, related_name="products_wishlist")

    def __str__(self):
        return f"{self.user_id}'s wishlist"

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"
