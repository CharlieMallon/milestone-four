# Generated by Django 4.0.1 on 2022-02-05 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_alter_order_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 21, 32, 40, 182232), null=True),
        ),
    ]
