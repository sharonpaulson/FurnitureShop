# Generated by Django 5.1.2 on 2024-11-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0008_orderdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='Product_Image',
            field=models.ImageField(blank=True, null=True, upload_to='cart_images'),
        ),
    ]
