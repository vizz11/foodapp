from django.contrib import admin
from .models import Order, OrderItem
from accounts.models import Account

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
# class customerItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ['product']
class Orders(admin.TabularInline):
    model = Account
    raw_id_fields = ['id']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','usid', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

