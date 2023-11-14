from django.db import models

class Purchase(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(unique=True, max_length=100)
    product_description = models.CharField(max_length=255, blank=True, null=True)
    product_image = models.CharField(max_length=255, blank=True, null=True)
    product_active = models.BooleanField(blank=True, null=True)
    product_spec_sheet = models.ForeignKey('ProductSpecSheet', models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'product'


class ProductInfo(models.Model):
    product_info = models.OneToOneField(Purchase, models.DO_NOTHING, related_name='product_i', primary_key=True)
    product_info_quantity = models.IntegerField()
    product_info_cost = models.DecimalField(max_digits=19, decimal_places=2)
    product_info_price = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        #managed = False
        db_table = 'product_info'


class ProductSpecSheet(models.Model):
    product_spec_sheet_id = models.AutoField(primary_key=True)
    product_spec_sheet_dir = models.CharField(unique=True, max_length=255)
    product_spec_sheet_active = models.BooleanField(blank=True, null=True) 

    class Meta:
        #managed = False
        db_table = 'product_spec_sheet'
