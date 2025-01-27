from rest_framework import serializers
from .models import *


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    ID = serializers.IntegerField(source='supplier_id')
    ID_Card = serializers.CharField(source='supplier_id_card')
    Name= serializers.CharField(source='supplier_name')
    Active = serializers.BooleanField(source='supplier_active')
    Comment = serializers.CharField(source='supplier_comment')
    class Meta:
        model = Supplier
        fields = ['ID', 'ID_Card', 'Name', 'Active', 'Comment']