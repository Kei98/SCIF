# Generated by Django 4.2.6 on 2024-05-08 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        ('product', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesDetail',
            fields=[
                ('sales_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('sales_detail_prod_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('sales_detail_tax', models.DecimalField(decimal_places=2, max_digits=19)),
                ('sales_detail_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('sales_detail_quantity', models.IntegerField()),
                ('sales_detail_subtotal', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
            options={
                'db_table': 'sales_detail',
            },
        ),
        migrations.AddField(
            model_name='salesdetail',
            name='product_s',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='product.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesdetail',
            name='sales',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='sales.sales'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesdetail',
            name='service_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='service.servicedetail'),
        ),
    ]
