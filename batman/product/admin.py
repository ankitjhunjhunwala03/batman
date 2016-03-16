from django.contrib import admin
from models import Product, Attribute, Category, AttributeValue, Variation, ProductImage
# Register your models here.

admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(ProductImage)
