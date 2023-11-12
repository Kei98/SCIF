from rest_framework import serializers
from .models import *


class ProductSpecSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecSheet
        fields = '__all__'


class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    product_i = ProductInfoSerializer(read_only=True)
    _spec_sheet= serializers.CharField(source='product_spec_sheet.product_spec_sheet_dir')
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_description', 
                  'product_image', 'product_i', '_spec_sheet', 'product_active']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
