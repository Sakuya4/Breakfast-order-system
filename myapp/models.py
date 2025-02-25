from django.db import models

class OrderProduct(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    cart_item = models.JSONField()
    total_price = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"