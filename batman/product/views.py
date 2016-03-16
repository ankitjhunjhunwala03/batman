from django.shortcuts import render
from django.views.generic import TemplateView
from models import Variation

# Create your views here.


class HomePage(TemplateView):
    template_name = "product/index.html"

    def get_context_data(self, **kwargs):
        kwargs['products'] = Variation.objects.all()
        return kwargs


class Product(TemplateView):
    template_name = "product/product.html"

    def get_context_data(self, **kwargs):
        kwargs['products'] = Variation.objects.all()
        return kwargs
