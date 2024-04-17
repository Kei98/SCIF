from rest_framework import serializers
from .models import *
from django.contrib.auth import (
    get_user_model,
    authenticate
    )
from django.utils.translation import gettext as _

class UserRoleSerializer(serializers.ModelSerializer):
    # user_r=UserSerializer(read_only=True, many=True)
    class Meta:
        model = UserRole
        fields = ['user_role_id', 'user_role_name', 'user_role_active']


#Get all
class UsersSerializer(serializers.ModelSerializer):
    # get the user role name for each user
    user_role = serializers.CharField(source='role.user_role_name')

    class Meta:
        model = User
        fields = ['id', 'email', 'user_active', 'role', 'user_role']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'min_length':8}}

    def create(self, validated_data):
        print('validated_data')
        print(validated_data)
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token"""
    email = serializers.EmailField()
    password= serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs

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
