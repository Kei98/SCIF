from django.db import models

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_id_card = models.CharField(unique=True, max_length=12)
    supplier_name = models.CharField(max_length=30)
    supplier_active = models.BooleanField(blank=True, null=True)
    supplier_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'supplier'

