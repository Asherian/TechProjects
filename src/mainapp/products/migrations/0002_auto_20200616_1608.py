# Generated by Django 3.0.7 on 2020-06-16 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetizers'), ('drinks', 'drinks'), ('entrees', 'entrees')], max_length=60),
        ),
    ]