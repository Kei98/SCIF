from rest_framework import serializers
from .models import *
from supplier.serializers import SupplierSerializer


class PurchasesSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    _user = serializers.CharField(
        source='user.user_id.user_info_name', read_only=True)

    class Meta:
        model = Purchase
        fields = [
            'purchase_id',
            'purchase_number',
            'purchase_date',
            'purchase_subtotal',
            'purchase_tax',
            'purchasediscount',
            'purchase_amount',
            'purchase_active',
            'supplier',
            '_user'
        ]


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class PurchaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetail
        fields = '__all__'


class PurchaseDetailsSerializer(serializers.ModelSerializer):
    _product = serializers.CharField(
        source='product.product_name', read_only=True)

    class Meta:
        model = PurchaseDetail
        fields = [
            'purchase_detail_id',
            'purchase_detail_prod_price',
            'purchase_detail_tax',
            'purchase_detail_discount',
            'purchase_detail_quantity',
            'purchase_detail_subtotal',
            '_product',
            'purchase'
        ]


class InventoryPurchaseSerializer(serializers.ModelSerializer):
    PProduct = serializers.CharField(
        source='product.product_name', read_only=True)
    PDate = serializers.DateTimeField(
        source='purchase.purchase_date', read_only=True)
    PQuantity = serializers.IntegerField(
        source='purchase_detail_quantity', read_only=True)

    class Meta:
        model = PurchaseDetail
        fields = [
            'PDate',
            'PProduct',
            'PQuantity'
        ]

class ReportPurchaseSerializer(serializers.ModelSerializer):
    PDate = serializers.DateTimeField(
        source='purchase_date', read_only=True)
    PSubtotal = serializers.DecimalField(max_digits=19, decimal_places=2,
        source='purchase_subtotal', read_only=True)
    PTax = serializers.DecimalField(max_digits=19, decimal_places=2,
        source='purchase_tax', read_only=True)
    PDiscount = serializers.DecimalField(max_digits=19, decimal_places=2,
        source='purchase_discount', read_only=True)
    PAmount = serializers.DecimalField(max_digits=19, decimal_places=2,
        source='purchase_amount', read_only=True)
    PActive = serializers.BooleanField(
        source='purchase_active', read_only=True)

    class Meta:
        model = Purchase
        fields = [
            'PDate',
            'PSubtotal',
            'PTax',
            'PDiscount',
            'PAmount',
            'PActive'
        ]