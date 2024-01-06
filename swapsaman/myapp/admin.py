from django.contrib import admin
from myapp.models import *

# Register your models here.
admin.site.site_header = "SwapSaman | Admin"

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(BuyerPrice)