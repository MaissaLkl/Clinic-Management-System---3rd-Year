# Generated by Django 5.1.4 on 2025-01-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_category_supplier_inventory_log_surgery_type_surgery'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='fee',
            field=models.CharField(default=200, max_length=100),
            preserve_default=False,
        ),
    ]
