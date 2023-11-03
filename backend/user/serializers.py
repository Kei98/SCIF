from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'user_email',
                  'user_password', 'user_active', 'user_role']
        
class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['user_info_id', 'user_info_name', 'user_info_id_card', 'user_info_tel_number', 
                  'user_info_email', 'user_info_address', 'user_info_active']
        
class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserContact
        fields = ['user_contact_id', 'user_contact_number', 'user_contact_name', 
                  'user_contact_active', 'user_info']
        
class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserRole
        fields = ['user_role_id', 'user_role_name', 'user_role_active']