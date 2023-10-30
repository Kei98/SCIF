from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    print("Llega al UserSerializer class")
    class Meta:
        print("Defines User")
        model = User
        print("Defines fields")
        fields = ['user_id', 'user_name', 'user_email', 'user_password', 'user_active', 'user_role', 'user_info']
        print("Fields defined")