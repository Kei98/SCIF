# Generated by Django 4.2.6 on 2023-11-14 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_alter_user_user_id_alter_usercontact_user_info'),
        ('product', '0002_alter_product_product_id_and_more'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_number', models.CharField(max_length=23, unique=True)),
                ('purchase_date', models.DateTimeField()),
                ('purchase_subtotal', models.DecimalField(decimal_places=2, max_digits=19)),
                ('purchase_tax', models.DecimalField(decimal_places=2, max_digits=19)),
                ('purchasediscount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('purchase_amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('purchase_active', models.BooleanField(blank=True, null=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='supplier.supplier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
            options={
                'db_table': 'purchase',
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('purchase_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_detail_prod_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('purchase_detail_tax', models.DecimalField(decimal_places=2, max_digits=19)),
                ('purchase_detail_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('purchase_detail_quantity', models.IntegerField()),
                ('purchase_detail_subtotal', models.DecimalField(decimal_places=2, max_digits=19)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='purchase.purchase')),
            ],
            options={
                'db_table': 'purchase_detail',
            },
        ),
    ]