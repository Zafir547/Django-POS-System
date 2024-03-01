# Generated by Django 5.0.2 on 2024-03-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(blank=True, max_length=256, null=True)),
                ('address', models.TextField(blank=True, max_length=256, null=True)),
                ('email', models.EmailField(blank=True, max_length=256, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'Customers',
            },
        ),
    ]