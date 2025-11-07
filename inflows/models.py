from django.db import models

from products.models import Product
from suppliers.models import Supplier


class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows', verbose_name='Fornecedor')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows', verbose_name='Produto')
    quantity = models.IntegerField(verbose_name='Quantidade')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Entrada'

    def __str__(self):
        return str(self.product)
