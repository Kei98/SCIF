from django.db import models

class Quote(models.Model):
    quote_id = models.AutoField(primary_key=True)
    quote_request = models.CharField(max_length=255)
    quote_on_behalf_of = models.CharField(max_length=100, blank=True, null=True)
    quote_date = models.DateTimeField(blank=True, null=True)
    quote_active = models.BooleanField(blank=True, null=True) 
    user = models.ForeignKey('User', models.DO_NOTHING)
    quote_assigned_user = models.ForeignKey('User', models.DO_NOTHING, related_name='quote_quote_assigned_user_set', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'quote'


class QuoteAnswer(models.Model):
    quote_answer_id = models.AutoField(primary_key=True)
    quote_answer_description = models.CharField(max_length=255)
    quote_answer_date = models.DateTimeField(blank=True, null=True)
    quote_answer_active = models.BooleanField(blank=True, null=True) 
    quote = models.ForeignKey(Quote, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    service_detail = models.ForeignKey('ServiceDetail', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'quote_answer'
