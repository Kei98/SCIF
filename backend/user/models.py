from typing import Any
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class AppUserManager(BaseUserManager):
    def create_user(self, id, email, role, password=None, **extra_fields):
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        if not id:
            raise ValueError('A user id is required')
        if not role:
            raise ValueError('A user role is required')
        email1 = self.normalize_email(email)
        extra_fields['user_active'] = False
        user = self.model(email=email1, id=id, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, id, email, role, password=None):
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        if not id:
            raise ValueError('A user id is required')
        if not role:
            raise ValueError('A user role is required')
        user = self.create_user(email, id, role, password)
        user.user_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.OneToOneField('UserInfo', models.DO_NOTHING, related_name='_user', primary_key=True)
    email = models.EmailField(unique=True, max_length=50)
    # user_password = models.CharField(max_length=255, null=False)
    user_active = models.BooleanField(blank=True, null=True, default=False)
    role = models.ForeignKey('UserRole', models.DO_NOTHING)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = AppUserManager()

    class Meta:
        #managed = False
        db_table = 'user'

# class User(models.Model):
#     user_id = models.OneToOneField('UserInfo', models.DO_NOTHING, related_name='_user', primary_key=True)
#     user_name = models.CharField(unique=True, max_length=20)
#     user_email = models.CharField(unique=True, max_length=30)
#     user_password = models.CharField(max_length=255)
#     user_active = models.BooleanField(blank=True, null=True)
#     user_role = models.ForeignKey('UserRole', models.DO_NOTHING)

#     class Meta:
#         #managed = False
#         db_table = 'user'


class UserContact(models.Model):
    user_contact_id = models.AutoField(primary_key=True)
    user_contact_number = models.CharField(unique=True, max_length=12)
    user_contact_name = models.CharField(max_length=255)
    user_contact_active = models.BooleanField(blank=True, null=True)
    user_info = models.ForeignKey('UserInfo', models.DO_NOTHING, related_name='user_c')

    class Meta:
        #managed = False
        db_table = 'user_contact'


class UserInfo(models.Model):
    user_info_id = models.AutoField(primary_key=True)
    user_info_name = models.CharField(max_length=255)
    user_info_id_card = models.CharField(unique=True, max_length=12)
    user_info_tel_number = models.CharField(unique=True, max_length=12)
    user_info_email = models.EmailField(unique=True, max_length=30)
    user_info_address = models.CharField(max_length=255)
    user_info_active = models.BooleanField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'user_info'


class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user_role_name = models.CharField(unique=True, max_length=20)
    user_role_active = models.BooleanField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'user_role'
