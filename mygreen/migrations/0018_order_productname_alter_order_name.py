# Generated by Django 4.0 on 2021-12-23 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygreen', '0017_alter_order_paymentmode'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='productname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
