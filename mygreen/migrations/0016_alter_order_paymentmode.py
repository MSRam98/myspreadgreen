# Generated by Django 4.0 on 2021-12-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygreen', '0015_order_paymentmode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paymentmode',
            field=models.CharField(max_length=25, null=True),
        ),
    ]