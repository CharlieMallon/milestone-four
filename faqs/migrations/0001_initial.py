# Generated by Django 4.0.1 on 2022-01-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_title', models.CharField(max_length=254)),
                ('faq_content', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'faqs',
            },
        ),
    ]
