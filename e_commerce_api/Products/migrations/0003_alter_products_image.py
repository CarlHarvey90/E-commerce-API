# Generated by Django 5.2 on 2025-05-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
