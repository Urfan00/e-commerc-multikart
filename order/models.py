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


class Basket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id.username}'s {self.id}-{self.is_active} basket"

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"


class BasketItem(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    product_version_id = models.ForeignKey(ProductVersion, on_delete = models.CASCADE, related_name="product_basket_item")
    basket_id = models.ForeignKey(Basket, on_delete = models.CASCADE, related_name="basket_items")

    def __str__(self):
        return f"{self.basket_id.user_id.username}'s basket item"

    class Meta:
        verbose_name = "Basket Item"
        verbose_name_plural = "Basket Items"

    def get_subtotal(self):
        if self.product_version_id.product_id.in_sale:
            subtotal = self.product_version_id.product_id.new_price * self.quantity
        else:
            subtotal = self.product_version_id.product_id.price * self.quantity
        return subtotal
