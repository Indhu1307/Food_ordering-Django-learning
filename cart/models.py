
from django.db import models  # creating table in db
from django.conf import settings # project setting user model access
from menu.models import Food  # connecting menu to cart


class Cart(models.Model):
    user = models.OneToOneField( # displayed only one cart to one user
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True) # storing date and time

    def __str__(self): 
        return f"{self.user.username}'s Cart"

class CartItem(models.Model): # another class for cart item
    cart = models.ForeignKey( # conneting to cart
        Cart,
        on_delete=models.CASCADE,  # if cart is deleted cart item alse deleted
        related_name='items' #easy 
    )
    food = models.ForeignKey( # connecting menu/ models.py
        Food,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [  # database follows restri
            models.UniqueConstraint(
                fields=['cart', 'food'],
                name='unique_food_per_cart'  #dosa_paneer
            )
        ]

    def __str__(self):
        return f"{self.food.food_name} - {self.quantity}"
