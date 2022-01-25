# Generated by Django 4.0.1 on 2022-01-25 16:00

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_country_alter_order_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='county',
            field=django_countries.fields.CountryField(default='GBR', max_length=2),
        ),
    ]