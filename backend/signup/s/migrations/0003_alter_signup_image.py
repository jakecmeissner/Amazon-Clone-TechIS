# Generated by Django 4.1.1 on 2022-11-11 22:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s', '0002_signup_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
