from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from menu.models import Dish


class Order(models.Model):
    taken_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    table_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Tavolo {self.table_number} - {self.created_at.strftime('%d/%m %H:%M')} - Fatto da {self.taken_by.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name="items",
                              on_delete=models.RESTRICT)
    dish = models.ForeignKey(Dish, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.dish.name} x {self.quantity}"
