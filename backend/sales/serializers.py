from rest_framework import serializers
from .models import *
from service.serializers import ServiceDetsSerializer, ServicesSerializerGet
from product.serializers import ProductInfoSerializerGet
from purchase.serializers import ReportPurchaseSerializer
from purchase.models import PurchaseDetail


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class SalesStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesStatus
        fields = '__all__'

class InventoryReportSerializer(serializers.Serializer):
    Product=serializers.CharField(max_length=255)
    Date= serializers.DateTimeField(format="%Y-%m-%d")
    Quantity= serializers.DecimalField(max_digits=19, decimal_places=2)



class SalesReportSerializer(serializers.Serializer):
    ID=serializers.IntegerField()
    Date= serializers.DateTimeField(format="%Y-%m-%d")
    Total= serializers.DecimalField(max_digits=19, decimal_places=2)

class ReportSerializer(serializers.ModelSerializer):
    Purchase = ReportPurchaseSerializer(read_only=True)
    Date = serializers.DateTimeField(
        source='sales_date', read_only=True)
    Subtotal = serializers.DecimalField(max_digits=19, decimal_places=2,
        source='sales_subtotal', read_only=True)
    Tax = serializers.DecimalField(max_digits=19, decimal_places=2,
        source='sales_tax', read_only=True)
    Discount = serializers.DecimalField(max_digits=19, decimal_places=2,
        source='sales_discount', read_only=True)
    Amount = serializers.DecimalField(max_digits=19, decimal_places=2,
        source='sales_amount', read_only=True)
    Status = serializers.CharField(
        source='sales_status.sales_status_name', read_only=True)

    class Meta:
        model = Sales
        fields = [
            'Date',
            'Subtotal',
            'Tax',
            'Discount',
            'Amount',
            'Status',
            'Purchase'

        ]


class SalessSerializer(serializers.ModelSerializer):
    ID = serializers.IntegerField(source='sales_id')
    Date = serializers.DateTimeField(source='sales_date', format="%Y-%m-%d")
    Subtotal = serializers.DecimalField(source='sales_subtotal', max_digits=19, decimal_places=2)
    Tax = serializers.DecimalField(source='sales_tax', max_digits=19, decimal_places=2)
    Discount = serializers.DecimalField(source='sales_discount', max_digits=19, decimal_places=2)
    Amount = serializers.DecimalField(source='sales_amount', max_digits=19, decimal_places=2)
    User = serializers.CharField(
        source='user', read_only=True)
    Payment = serializers.CharField(
        source='payment_method.payment_method_name', read_only=True)
    Status = serializers.CharField(
        source='sales_status.sales_status_name', read_only=True)

    class Meta:
        model = Sales
        fields = [
            'ID',
            'Date',
            'Subtotal',
            'Tax',
            'Discount',
            'Amount',
            'User',
            'Payment',
            'Status'
        ]


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


class SalesSerializerGet(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user', read_only=True)
    payment = serializers.CharField(source='payment_method.payment_method_name', read_only=True)
    status = serializers.CharField(source='sales_status.sales_status_name', read_only=True)

    class Meta:
        model = Sales
        fields = '__all__'
        extra_fields = ['user_name', 'payment', 'status']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        for field in self.Meta.extra_fields:
            representation[field] = getattr(instance, field, None)
        return representation

class SalesDetsSerializer(serializers.ModelSerializer):
    Product = serializers.CharField(
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
            'Product',
            'sales',
            'service_detail'
        ]


class SalesDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDetail
        fields = '__all__'

class SalesDetsSerializer(serializers.ModelSerializer):
    ID=serializers.IntegerField(source='sales_detail_id')
    Price=serializers.DecimalField(source='sales_detail_prod_price', max_digits=19, decimal_places=2)
    Tax=serializers.DecimalField(source='sales_detail_tax', max_digits=19, decimal_places=2)
    Discount=serializers.DecimalField(source='sales_detail_discount', max_digits=19, decimal_places=2)
    Quantity=serializers.IntegerField(source='sales_detail_quantity')
    Subtotal=serializers.DecimalField(source='sales_detail_subtotal', max_digits=19, decimal_places=2)
    Product=serializers.CharField(source='product_s.product_name')
    Sale=serializers.IntegerField(source='sales.sales_id')
    Service=ServicesSerializerGet(read_only=True, source='service.service_name')
    class Meta:
        model = SalesDetail
        fields = ['ID','Price','Tax','Discount','Quantity','Subtotal','Product','Sale','Service']
