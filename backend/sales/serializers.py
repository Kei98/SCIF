from rest_framework import serializers
from .models import *
from service.serializers import ServiceDetsSerializer
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
    # Purchase = InventoryPurchaseSerializer(source='product_detail', read_only=True)
    # Product = serializers.CharField(
    #     source='product_s.product_name', read_only=True)
    # Quantity = serializers.IntegerField(
    #     source='sales_detail_quantity', read_only=True)
    # Date = serializers.DateTimeField(
    #     source='sales.sales_date', read_only=True)
    # Product = serializers.CharField(
    #     source='product.product_name', read_only=True)
    # PDate = serializers.DateTimeField(
    #     source='purchase.purchase_date', read_only=True)
    # PQuantity = serializers.IntegerField(
    #     source='purchase_detail_quantity', read_only=True)
    # id = serializers.IntegerField(primary_key=True)
    # for row in serializers:
    #         Producto=row[0],
    #         Fecha_Venta= row[1],
    #         Cantidad_Vendida= row[2],
    #         Fecha_Compra= row[3],
    #         Cantidad_Comprada= row[4]
    Producto=serializers.CharField(max_length=255)
    Fecha= serializers.DateTimeField()
    Cantidad= serializers.DecimalField(max_digits=19, decimal_places=2)
    # Fecha_Compra= serializers.DateTimeField()
    # Cantidad_Comprada= serializers.DecimalField(max_digits=19, decimal_places=2)

    # class Meta:
    #     model = InventoryReportModel
    #     fields = [
    #          'Producto',
    #          'Fecha_Venta',
    #          'Cantidad_Vendida',
    #          'Fecha_Compra',
    #          'Cantidad_Comprada'
    #          ]

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
