# Generated by Django 4.0 on 2021-12-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygreen', '0011_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]