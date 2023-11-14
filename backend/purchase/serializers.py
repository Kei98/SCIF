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
