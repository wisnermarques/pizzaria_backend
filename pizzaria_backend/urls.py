from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pizzas.views import PedidoViewSet, PizzaViewSet


router = DefaultRouter()
router.register(r'pizzas', PizzaViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
