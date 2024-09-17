from rest_framework import serializers
from .models import Pizza, Pedido, PedidoItem

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id', 'nome', 'descricao', 'preco']

class PedidoItemSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer(read_only=True)

    class Meta:
        model = PedidoItem
        fields = ['pizza', 'quantidade']

class PedidoSerializer(serializers.ModelSerializer):
    itens = PedidoItemSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'data_pedido', 'itens']
