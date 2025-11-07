from django.db import models

from products.models import Product


class Outflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='outflows', verbose_name='Produto')
    quantity = models.IntegerField(verbose_name='Quantidade')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Saída'

    def __str__(self):
        return str(self.product)
