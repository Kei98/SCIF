from django.db import models

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(unique=True, max_length=255)
    service_active = models.BooleanField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'service'


class ServiceDetail(models.Model):
    service_detail_id = models.AutoField(primary_key=True)
    service_detail_date = models.DateTimeField(blank=True, null=True)
    service_detail_description = models.CharField(max_length=255, blank=True, null=True)
    service_detail_subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    service_detail_tax = models.DecimalField(max_digits=19, decimal_places=2)
    service_detail_discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    service_detail_total = models.DecimalField(max_digits=19, decimal_places=2)
    service_detail_active = models.BooleanField(blank=True, null=True)
    service = models.ForeignKey(Service, models.DO_NOTHING, related_name='_service')

    class Meta:
        #managed = False
        db_table = 'service_detail'
