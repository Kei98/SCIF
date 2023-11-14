# from django.db import models
# from product.models import Product

# class PaymentMethod(models.Model):
#     payment_method_id = models.AutoField(primary_key=True)
#     payment_method_name = models.CharField(max_length=20, blank=True, null=True)
#     payment_method_info = models.CharField(max_length=255, blank=True, null=True)
#     payment_method_active = models.BooleanField(blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'payment_method'

# # is sales_active really necessary?
# class Sales(models.Model):
#     sales_id = models.AutoField(primary_key=True)
#     sales_date = models.DateTimeField()
#     sales_subtotal = models.DecimalField(max_digits=19, decimal_places=2)
#     sales_tax = models.DecimalField(max_digits=19, decimal_places=2)
#     sales_discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     sales_amount = models.DecimalField(max_digits=19, decimal_places=2)
#     sales_active = models.BooleanField(blank=True, null=True)
#     user = models.ForeignKey('User', models.DO_NOTHING)
#     payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING)
#     sales_status = models.ForeignKey('SalesStatus', models.DO_NOTHING)

#     class Meta:
#         #managed = False
#         db_table = 'sales'


# class SalesDetail(models.Model):
#     sales_detail_id = models.AutoField(primary_key=True)
#     sales_detail_prod_price = models.DecimalField(max_digits=19, decimal_places=2)
#     sales_detail_tax = models.DecimalField(max_digits=19, decimal_places=2)
#     sales_detail_discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     sales_detail_quantity = models.IntegerField()
#     sales_detail_subtotal = models.DecimalField(max_digits=19, decimal_places=2)
#     product = models.ForeignKey(Product, models.DO_NOTHING)
#     sales = models.ForeignKey(Sales, models.DO_NOTHING)
#     service_detail = models.ForeignKey('ServiceDetail', models.DO_NOTHING)

#     class Meta:
#         #managed = False
#         db_table = 'sales_detail'


# class SalesStatus(models.Model):
#     sales_status_id = models.AutoField(primary_key=True)
#     sales_status_name = models.CharField(unique=True, max_length=20)
#     sales_status_active = models.BooleanField(blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'sales_status'
