# Generated by Django 4.0 on 2021-12-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygreen', '0006_alter_customerdetail_profilepic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(blank=True, max_length=50, null=True)),
                ('productmenupic', models.ImageField(blank=True, default='profileimage.jpg', null=True, upload_to='')),
                ('productbuypic1', models.ImageField(blank=True, default='profileimage.jpg', null=True, upload_to='')),
                ('productbuypic2', models.ImageField(blank=True, default='profileimage.jpg', null=True, upload_to='')),
                ('productbuypic3', models.ImageField(blank=True, default='profileimage.jpg', null=True, upload_to='')),
                ('productbuypic4', models.ImageField(blank=True, default='profileimage.jpg', null=True, upload_to='')),
                ('productprice', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
