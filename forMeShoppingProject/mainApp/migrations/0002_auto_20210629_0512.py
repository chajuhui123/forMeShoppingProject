# Generated by Django 3.2.4 on 2021-06-29 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measure',
            old_name='crotch',
            new_name='rise',
        ),
        migrations.AlterField(
            model_name='item',
            name='shop_name',
            field=models.CharField(max_length=100),
        ),
    ]
