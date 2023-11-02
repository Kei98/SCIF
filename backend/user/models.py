from django.db import models

class User(models.Model):
    user_id = models.OneToOneField('UserInfo', models.DO_NOTHING, primary_key=True)
    user_name = models.CharField(unique=True, max_length=20)
    user_email = models.CharField(unique=True, max_length=30)
    user_password = models.CharField(max_length=255)
    user_active = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_role = models.ForeignKey('UserRole', models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'user'


class UserContact(models.Model):
    user_contact_id = models.AutoField(primary_key=True)
    user_contact_number = models.CharField(unique=True, max_length=12)
    user_contact_name = models.CharField(max_length=255)
    user_contact_active = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_info = models.ForeignKey('UserInfo', models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'user_contact'


class UserInfo(models.Model):
    user_info_id = models.AutoField(primary_key=True)
    user_info_name = models.CharField(max_length=255)
    user_info_id_card = models.CharField(unique=True, max_length=12)
    user_info_tel_number = models.CharField(unique=True, max_length=12)
    user_info_email = models.CharField(unique=True, max_length=30)
    user_info_address = models.CharField(max_length=255)
    user_info_active = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        #managed = False
        db_table = 'user_info'


class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user_role_name = models.CharField(unique=True, max_length=20)
    user_role_active = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
#        managed = False
        db_table = 'user_role'
