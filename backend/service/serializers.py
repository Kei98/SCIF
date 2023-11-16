from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    # user_r=UserSerializer(read_only=True, many=True)
    class Meta:
        model = Service
        fields = '__all__'


class ServiceDetsSerializer(serializers.ModelSerializer):
    # get the service object related to this user info
    _service = serializers.CharField(
        source='service.service_name', read_only=True)

    class Meta:
        model = ServiceDetail
        fields = [
            'service_detail_id',
            'service_detail_date',
            'service_detail_description',
            'service_detail_subtotal',
            'service_detail_tax',
            'service_detail_discount',
            'service_detail_total',
            'service_detail_active',
            '_service'
        ]


class ServiceDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetail
        fields = '__all__'
