from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Login)
admin.site.register(Buyer)
admin.site.register(Cart)
admin.site.register(Shipping_address)
admin.site.register(Bank)