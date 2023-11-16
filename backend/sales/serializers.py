from rest_framework import serializers
from .models import *
from service.serializers import ServiceDetsSerializer


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class SalesStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesStatus
        fields = '__all__'


class SalessSerializer(serializers.ModelSerializer):
    _user = serializers.CharField(
        source='user.user_id.user_info_name', read_only=True)
    _payment_method = serializers.CharField(
        source='payment_method.payment_method_name', read_only=True)
    _sales_status = serializers.CharField(
        source='sales_status.sales_status_name', read_only=True)

    class Meta:
        model = Sales
        fields = [
            'sales_id',
            'sales_date',
            'sales_subtotal',
            'sales_tax',
            'sales_discount',
            'sales_amount',
            '_user',
            '_payment_method',
            '_sales_status'
        ]


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


class SalesDetsSerializer(serializers.ModelSerializer):
    _product = serializers.CharField(
        source='product.product_name', read_only=True)
    service_detail = ServiceDetsSerializer(read_only=True)

    class Meta:
        model = SalesDetail
        fields = [
            'sales_detail_id',
            'sales_detail_prod_price',
            'sales_detail_tax',
            'sales_detail_discount',
            'sales_detail_quantity',
            'sales_detail_subtotal',
            '_product',
            'sales',
            'service_detail'
        ]


class SalesDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDetail
        fields = '__all__'
