# Generated by Django 4.2.3 on 2023-08-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_website', '0013_product_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(max_length=20),
        ),
    ]