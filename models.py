from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    STATUS_CHOICES = [
        ("AVAILABLE", "Available"),
        ("OCCUPIED", "Occupied"),
        ("BILL_REQUESTED", "Bill Requested"),
        ("CLOSED", "Closed"),
    ]

    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="AVAILABLE")

    def __str__(self):
        return f"Table {self.table_number}"


# ---------- MENU ----------
class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ("STARTER", "Starter"),
        ("MAIN", "Main"),
        ("DRINK", "Drink"),
        ("DESSERT", "Dessert"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS_CHOICES = [
        ("PLACED", "Placed"),
        ("IN_KITCHEN", "In Kitchen"),
        ("SERVED", "Served"),
    ]

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PLACED")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.table.status == "AVAILABLE":
            self.table.status = "OCCUPIED"
            self.table.save()
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Bill(models.Model):
    STATUS_CHOICES = [
        ("NOT_GENERATED", "Not Generated"),
        ("PENDING", "Pending Payment"),
        ("PAID", "Paid"),
    ]

    table = models.OneToOneField(Table, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="NOT_GENERATED")

    def mark_paid(self):
        self.status = "PAID"
        self.save()
        self.table.status = "AVAILABLE"
        self.table.save()
