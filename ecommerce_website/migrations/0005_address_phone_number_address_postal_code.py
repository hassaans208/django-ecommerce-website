# Generated by Django 4.2.3 on 2023-08-09 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_website', '0004_alter_address_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
