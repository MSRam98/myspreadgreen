# Generated by Django 4.0 on 2021-12-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygreen', '0007_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productprice',
            field=models.FloatField(blank=True, null=True),
        ),
    ]