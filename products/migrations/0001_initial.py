# Generated by Django 5.0.2 on 2024-03-01 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(max_length=256)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], max_length=100, verbose_name='Status of the category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(max_length=256)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], max_length=100, verbose_name='Status of the product')),
                ('price', models.FloatField(default=0)),
                ('category', models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.category')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
