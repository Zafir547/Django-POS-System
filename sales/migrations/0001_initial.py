# Generated by Django 5.0.2 on 2024-03-01 12:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('sub_total', models.FloatField(default=0)),
                ('grand_total', models.FloatField(default=0)),
                ('tax_amount', models.FloatField(default=0)),
                ('tax_percentage', models.FloatField(default=0)),
                ('amount_payed', models.FloatField(default=0)),
                ('amount_change', models.FloatField(default=0)),
                ('customer', models.ForeignKey(db_column='customer', on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer')),
            ],
            options={
                'db_table': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('total_detail', models.FloatField()),
                ('product', models.ForeignKey(db_column='product', on_delete=django.db.models.deletion.DO_NOTHING, to='products.product')),
                ('sale', models.ForeignKey(db_column='sale', on_delete=django.db.models.deletion.DO_NOTHING, to='sales.sale')),
            ],
            options={
                'db_table': 'SaleDetails',
            },
        ),
    ]
