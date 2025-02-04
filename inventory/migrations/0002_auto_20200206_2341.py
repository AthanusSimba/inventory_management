# Generated by Django 3.0.3 on 2020-02-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('Sold', 'Item Sold'), ('RESTOCKING', 'Item restocking in a few days')], default='SOLD', max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('Sold', 'Item Sold'), ('RESTOCKING', 'Item restocking in a few days')], default='SOLD', max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('Sold', 'Item Sold'), ('RESTOCKING', 'Item restocking in a few days')], default='SOLD', max_length=10),
        ),
    ]
