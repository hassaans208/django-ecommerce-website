# Generated by Django 4.2.3 on 2023-08-10 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_website', '0008_rename_brand_id_product_brand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
