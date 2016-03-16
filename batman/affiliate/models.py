from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Affiliate(models.Model):
    company = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Affiliate"
        verbose_name_plural = "Affiliates"

    def __str__(self):
        return self.company
