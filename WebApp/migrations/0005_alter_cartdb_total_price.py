# Generated by Django 5.1.2 on 2024-11-10 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_cartdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdb',
            name='Total_Price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]