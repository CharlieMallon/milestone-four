# Generated by Django 4.0.1 on 2022-01-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_category_image_url_remove_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gluten_free_option',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]