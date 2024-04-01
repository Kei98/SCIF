from rest_framework import serializers
from .models import *


class ProductSpecSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecSheet
        fields = '__all__'


class ProductInfoSerializerGet(serializers.ModelSerializer):
    Quantity = serializers.IntegerField(source='product_info_quantity')
    Cost = serializers.DecimalField(
        source='product_info_cost', max_digits=19, decimal_places=2)
    Price = serializers.DecimalField(
        source='product_info_price', max_digits=19, decimal_places=2)

    class Meta:
        model = ProductInfo
        fields = ['product_info', 'Quantity', 'Cost', 'Price']

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    ID = serializers.CharField(source='product_id')
    Name = serializers.CharField(source='product_name')
    Description = serializers.CharField(source='product_description')
    Image = serializers.CharField(source='product_image')
    Active = serializers.CharField(source='product_active')
    # Name = serializers.CharField(source='product_id')
    Info = ProductInfoSerializerGet(read_only=True, source='product_i')
    Spec = serializers.CharField(
        source='product_spec_sheet.product_spec_sheet_name')

    class Meta:
        model = Product
        fields = ['ID', 'Name', 'Description',
                  'Image', 'Info', 'Spec', 'Active']


class ProductSerializer(serializers.ModelSerializer):
    # ID = serializers.CharField(source='product_id', allow_null=True, allow_blank=True)
    # Name = serializers.CharField(source='product_name')
    # Description = serializers.CharField(source='product_description', allow_blank=True)
    # Image = serializers.CharField(source='product_image', allow_null=True, allow_blank=True)
    # Active = serializers.CharField(source='product_active')
    # # Name = serializers.CharField(source='product_id')
    # Spec = serializers.IntegerField(source='product_spec_sheet')

    class Meta:
        model = Product
        fields = '__all__'
        # ['ID', 'Name', 'Description',
        #           'Image', 'Spec', 'Active']
        
        
    #     {   "product_id":null,
    # "product_name": "hjsed",
    # "product_description":null,
    # "product_image":null,
    # "product_active": null,
    # "product_spec_sheet":1
    # }