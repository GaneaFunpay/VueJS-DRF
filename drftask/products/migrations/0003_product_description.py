# Generated by Django 3.2.12 on 2022-03-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_time_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]