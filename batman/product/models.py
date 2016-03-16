from __future__ import unicode_literals

from django.db import models
from treebeard.mp_tree import MP_Node

# Create your models here.


class Category(MP_Node):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='products')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Variation(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, related_name='variations')
    slug = models.SlugField()
    sku = models.CharField(max_length=20)
    affiliate_sku = models.CharField(max_length=20)
    affiliate_url = models.URLField()
    short_description = models.TextField()
    long_description = models.TextField()
    marked_price = models.DecimalField(
        default=0.0, decimal_places=2, max_digits=10)
    discounted_price = models.DecimalField(
        default=0.0, decimal_places=2, max_digits=10)
    num_in_stock = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Variation"
        verbose_name_plural = "Variations"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    variation = models.ForeignKey(Variation, related_name='images')
    image = models.ImageField()
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = "ProductImage"
        verbose_name_plural = "ProductImages"

    def __str__(self):
        return self.variation.name


class Attribute(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Attribute"
        verbose_name_plural = "Attributes"

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=255)
    product = models.ForeignKey(Variation, related_name='attributes')

    class Meta:
        verbose_name = "AttributeValue"
        verbose_name_plural = "AttributeValues"

    def __str__(self):
        return self.name
