from django.contrib import admin
from .models import Table, MenuItem, Order, OrderItem, Bill

admin.site.register(Table)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Bill)
