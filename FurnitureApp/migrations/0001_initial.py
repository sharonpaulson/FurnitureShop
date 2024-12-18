# Generated by Django 5.1.2 on 2024-10-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Category_Description', models.TextField(blank=True, max_length=200, null=True)),
                ('Category_Image', models.ImageField(blank=True, null=True, upload_to='category_images')),
            ],
        ),
    ]
