# Generated by Django 4.2.6 on 2024-03-26 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100, unique=True)),
                ('product_description', models.CharField(blank=True, max_length=255, null=True)),
                ('product_image', models.CharField(blank=True, max_length=255, null=True)),
                ('product_active', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductSpecSheet',
            fields=[
                ('product_spec_sheet_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_spec_sheet_name', models.CharField(max_length=100, null=True, unique=True)),
                ('product_spec_sheet_dir', models.CharField(max_length=255, unique=True)),
                ('product_spec_sheet_active', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_spec_sheet',
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('product_info', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='product_i', serialize=False, to='product.product')),
                ('product_info_quantity', models.IntegerField()),
                ('product_info_cost', models.DecimalField(decimal_places=2, max_digits=19)),
                ('product_info_price', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
            options={
                'db_table': 'product_info',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_spec_sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.productspecsheet'),
        ),
    ]
