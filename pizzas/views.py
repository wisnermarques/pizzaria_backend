from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Pizza, Pedido, PedidoItem
from .serializers import PedidoSerializer, PizzaSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def create(self, request, *args, **kwargs):
        items = request.data.get('items')
        if not items:
            return Response({'error': 'Nenhum item no pedido'}, status=status.HTTP_400_BAD_REQUEST)

        # Criação do pedido
        pedido = Pedido.objects.create()

        # Adiciona cada item no pedido
        for item in items:
            pizza_id = item['pizza_id']
            quantity = item['quantity']
            try:
                pizza = Pizza.objects.get(id=pizza_id)
                PedidoItem.objects.create(pedido=pedido, pizza=pizza, quantidade=quantity)
            except Pizza.DoesNotExist:
                return Response({'error': f'Pizza com id {pizza_id} não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
