from django.db import models
from product.models import Purchase

class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    purchase_number = models.CharField(unique=True, max_length=23)
    purchase_date = models.DateTimeField()
    purchase_subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    purchase_tax = models.DecimalField(max_digits=19, decimal_places=2)
    purchasediscount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    purchase_amount = models.DecimalField(max_digits=19, decimal_places=2)
    purchase_active = models.BooleanField(blank=True, null=True)  
    supplier = models.ForeignKey('supplier.Supplier', models.DO_NOTHING)
    user = models.ForeignKey('user.User', models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'purchase'


class PurchaseDetail(models.Model):
    purchase_detail_id = models.AutoField(primary_key=True)
    purchase_detail_prod_price = models.DecimalField(max_digits=19, decimal_places=2)
    purchase_detail_tax = models.DecimalField(max_digits=19, decimal_places=2)
    purchase_detail_discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    purchase_detail_quantity = models.IntegerField()
    purchase_detail_subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    product = models.ForeignKey(Purchase, models.DO_NOTHING, related_name= '_product')
    purchase = models.ForeignKey(Purchase, models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'purchase_detail'
