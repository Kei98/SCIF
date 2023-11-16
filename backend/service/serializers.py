from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    # user_r=UserSerializer(read_only=True, many=True)
    class Meta:
        model = Service
        fields = '__all__'

class ServiceDetsSerializer(serializers.ModelSerializer):
    # get the user object related to this user info
    _service = serializers.CharField(source='service.service_name', read_only=True)

    class Meta:
        model = ServiceDetail
        fields = '__all__'


class ServiceDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetail
        fields = '__all__'