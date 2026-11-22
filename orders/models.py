from django.db import models  #craeting table in db
from django.conf import settings #access setting user model
from menu.models import Food # accessing menu/ food


class Order(models.Model): # creating models / class

    STATUS_CHOICES = [  # user identification
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Preparing', 'Preparing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    address = models.TextField()
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    food = models.ForeignKey(
        Food,
        on_delete=models.SET_NULL,  #while ordering food is deleted it should also delete in orderitem
        null=True
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"Order #{self.order.id} - {self.quantity}"



