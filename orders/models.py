from django.db import models
from drink.models import Drink
from django.contrib.auth.models import User

# Create your models here.
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Drink, on_delete=models.CASCADE, null=True, blank=True)
    # order = models.ForeignKey(Orders, on_delete=models.CASCADE,related_name="items_ordered", null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.item.name
    @property
    def get_total_item_price(self):
        return self.quantity * self.item.price
    
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    items_ordered = models.ManyToManyField(OrderItem,related_name="items_ordered")
    # total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return f'Order from {self.user.username}'