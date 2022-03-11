from django.contrib import admin
from .models import Variant,Product,ProductImage,ProductVariantPrice,ProductVariant
# Register your models here.
admin.site.register(Variant)
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(ProductVariantPrice)
admin.site.register(ProductVariant)