# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LogBook(models.Model):
    log_book_id = models.IntegerField(primary_key=True)
    log_book_action = models.CharField(max_length=255)
    log_book_user = models.IntegerField()
    log_book_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_book'


# class PaymentMethod(models.Model):
#     payment_method_id = models.IntegerField(primary_key=True)
#     payment_method_name = models.CharField(max_length=20, blank=True, null=True)
#     payment_method_info = models.CharField(max_length=255, blank=True, null=True)
#     payment_method_active = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'payment_method'


# class Product(models.Model):
#     product_id = models.IntegerField(primary_key=True)
#     product_name = models.CharField(unique=True, max_length=100)
#     product_description = models.CharField(max_length=255, blank=True, null=True)
#     product_image = models.CharField(max_length=255, blank=True, null=True)
#     product_active = models.TextField(blank=True, null=True)  # This field type is a guess.
#     product_spec_sheet = models.ForeignKey('ProductSpecSheet', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'product'


# class ProductInfo(models.Model):
#     product_info = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)
#     product_info_quantity = models.IntegerField()
#     product_info_cost = models.DecimalField(max_digits=19, decimal_places=2)
#     product_info_price = models.DecimalField(max_digits=19, decimal_places=2)

#     class Meta:
#         managed = False
#         db_table = 'product_info'


# class ProductSpecSheet(models.Model):
#     product_spec_sheet_id = models.IntegerField(primary_key=True)
#     product_spec_sheet_dir = models.CharField(unique=True, max_length=255)
#     product_spec_sheet_active = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'product_spec_sheet'


# class Purchase(models.Model):
#     purchase_id = models.IntegerField(primary_key=True)
#     purchase_number = models.CharField(unique=True, max_length=23)
#     purchase_date = models.DateTimeField()
#     purchase_subtotal = models.DecimalField(max_digits=19, decimal_places=2)
#     purchase_tax = models.DecimalField(max_digits=19, decimal_places=2)
#     purchasediscount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     purchase_amount = models.DecimalField(max_digits=19, decimal_places=2)
#     purchase_active = models.TextField(blank=True, null=True)  # This field type is a guess.
#     supplier = models.ForeignKey('Supplier', models.DO_NOTHING)
#     user = models.ForeignKey('User', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'purchase'


# class PurchaseDetail(models.Model):
#     purchase_detail_id = models.IntegerField(primary_key=True)
#     purchase_detail_prod_price = models.DecimalField(max_digits=19, decimal_places=2)
#     purchase_detail_tax = models.DecimalField(max_digits=19, decimal_places=2)
#     purchase_detail_discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     purchase_detail_quantity = models.IntegerField()
#     purchase_detail_subtotal = models.DecimalField(max_digits=19, decimal_places=2)
#     product = models.ForeignKey(Product, models.DO_NOTHING)
#     purchase = models.ForeignKey(Purchase, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'purchase_detail'


# class Quote(models.Model):
#     quote_id = models.IntegerField(primary_key=True)
#     quote_request = models.CharField(max_length=255)
#     quote_on_behalf_of = models.CharField(max_length=100, blank=True, null=True)
#     quote_date = models.DateTimeField(blank=True, null=True)
#     quote_active = models.TextField(blank=True, null=True)  # This field type is a guess.
#     user = models.ForeignKey('User', models.DO_NOTHING)
#     quote_assigned_user = models.ForeignKey('User', models.DO_NOTHING, related_name='quote_quote_assigned_user_set', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'quote'


# class QuoteAnswer(models.Model):
#     quote_answer_id = models.IntegerField(primary_key=True)
#     quote_answer_description = models.CharField(max_length=255)
#     quote_answer_date = models.DateTimeField(blank=True, null=True)
#     quote_answer_active = models.TextField(blank=True, null=True)  # This field type is a guess.
#     quote = models.ForeignKey(Quote, models.DO_NOTHING)
#     user = models.ForeignKey('User', models.DO_NOTHING)
#     service_detail = models.ForeignKey('ServiceDetail', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'quote_answer'


# class Sales(models.Model):
#     sales_id = models.IntegerField(primary_key=True)
#     sales_date = models.DateTimeField()
#     sales_subtotal = models.DecimalField(max_digits=19, decimal_places=2)
#     sales_tax = models.DecimalField(max_digits=19, decimal_places=2)
#     sales_discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     sales_amount = models.DecimalField(max_digits=19, decimal_places=2)
#     sales_active = models.TextField(blank=True, null=True)  # This field type is a guess.
#     user = models.ForeignKey('User', models.DO_NOTHING)
#     payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING)
#     sales_status = models.ForeignKey('SalesStatus', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'sales'


# class SalesDetail(models.Model):
#     sales_detail_id = models.IntegerField(primary_key=True)
#     sales_detail_prod_price = models.DecimalField(max_digits=19, decimal_places=2)
#     sales_detail_tax = models.DecimalField(max_digits=19, decimal_places=2)
#     sales_detail_discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     sales_detail_quantity = models.IntegerField()
#     sales_detail_subtotal = models.DecimalField(max_digits=19, decimal_places=2)
#     product = models.ForeignKey(Product, models.DO_NOTHING)
#     sales = models.ForeignKey(Sales, models.DO_NOTHING)
#     service_detail = models.ForeignKey('ServiceDetail', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'sales_detail'


# class SalesStatus(models.Model):
#     sales_status_id = models.IntegerField(primary_key=True)
#     sales_status_name = models.CharField(unique=True, max_length=20)
#     sales_status_active = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'sales_status'


# class Service(models.Model):
#     service_id = models.IntegerField(primary_key=True)
#     service_name = models.IntegerField(unique=True)
#     service_active = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'service'


# class ServiceDetail(models.Model):
#     service_detail_id = models.IntegerField(primary_key=True)
#     service_detail_date = models.DateTimeField(blank=True, null=True)
#     service_detail_description = models.CharField(max_length=255, blank=True, null=True)
#     service_detail_subtotal = models.DecimalField(max_digits=19, decimal_places=2)
#     service_detail_tax = models.DecimalField(max_digits=19, decimal_places=2)
#     service_detail_discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     service_detail_total = models.DecimalField(max_digits=19, decimal_places=2)
#     service = models.ForeignKey(Service, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'service_detail'


# class Supplier(models.Model):
#     supplier_id = models.IntegerField(primary_key=True)
#     supplier_id_card = models.CharField(unique=True, max_length=12)
#     supplier_name = models.CharField(max_length=30)
#     supplier_active = models.TextField(blank=True, null=True)  # This field type is a guess.
#     supplier_comment = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'supplier'


# class User(models.Model):
#     user = models.OneToOneField('UserInfo', models.DO_NOTHING, primary_key=True)
#     user_name = models.CharField(unique=True, max_length=20)
#     user_email = models.CharField(unique=True, max_length=30)
#     user_password = models.CharField(max_length=255)
#     user_active = models.TextField(blank=True, null=True)  # This field type is a guess.
#     user_role = models.ForeignKey('UserRole', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'user'


# class UserContact(models.Model):
#     user_contact_id = models.IntegerField(primary_key=True)
#     user_contact_number = models.CharField(unique=True, max_length=12)
#     user_contact_name = models.CharField(max_length=255)
#     user_contact_active = models.TextField(blank=True, null=True)  # This field type is a guess.
#     user_info = models.ForeignKey('UserInfo', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'user_contact'


# class UserInfo(models.Model):
#     user_info_id = models.IntegerField(primary_key=True)
#     user_info_name = models.CharField(max_length=255)
#     user_info_id_card = models.CharField(unique=True, max_length=12)
#     user_info_tel_number = models.CharField(unique=True, max_length=12)
#     user_info_email = models.CharField(unique=True, max_length=30)
#     user_info_address = models.CharField(max_length=255)
#     user_info_active = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'user_info'


# class UserRole(models.Model):
#     user_role_id = models.IntegerField(primary_key=True)
#     user_role_name = models.CharField(unique=True, max_length=20)
#     user_role_active = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'user_role'
