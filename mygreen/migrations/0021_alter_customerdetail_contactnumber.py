# Generated by Django 4.0 on 2021-12-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygreen', '0020_alter_customerdetail_contactnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetail',
            name='contactnumber',
            field=models.CharField(blank=True, default='contactnum', max_length=10, null=True),
        ),
    ]
