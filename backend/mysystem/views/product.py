from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer

from mysystem.models import Product
from utils.serializers import CustomModelSerializer
from utils.viewset import CustomModelViewSet


class ProductSerializer(CustomModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# 测试
class ProductViewSet(CustomModelViewSet):
    queryset = Product.objects.filter(is_active=True).order_by('-create_time')
    serializer_class = ProductSerializer
    # search_fields = ('name',)
    # filterset_class = ('is_active','price')