# Generated by Django 4.0.1 on 2022-02-06 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0016_alter_order_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 11, 50, 55, 274414), null=True),
        ),
    ]