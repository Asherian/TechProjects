# Generated by Django 3.0.7 on 2020-06-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200620_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('treats', 'treats'), ('appetizers', 'appetizers'), ('entrees', 'entrees')], max_length=60),
        ),
    ]