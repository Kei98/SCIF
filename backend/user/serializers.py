from rest_framework import serializers
from .models import *


class UserRoleSerializer(serializers.ModelSerializer):
    # user_r=UserSerializer(read_only=True, many=True)
    class Meta:
        model = UserRole
        fields = ['user_role_id', 'user_role_name', 'user_role_active']


class UsersSerializer(serializers.ModelSerializer):
    # get the user role name for each user
    _user_role = serializers.CharField(source='user_role.user_role_name')

    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'user_email',
                  'user_password', 'user_active', '_user_role']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    # get the user object related to this user info
    _user = UsersSerializer(read_only=True)

    class Meta:
        model = UserInfo
        fields = '__all__'


class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        fields = ['user_contact_id', 'user_contact_number', 'user_contact_name',
                  'user_contact_active', 'user_info']
