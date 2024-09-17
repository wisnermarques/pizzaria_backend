from django.db import models

class Pizza(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido {self.id}'

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, related_name='pedido_itens', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantidade}x {self.pizza.nome}'
