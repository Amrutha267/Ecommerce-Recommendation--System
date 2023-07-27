# Generated by Django 4.1.7 on 2023-03-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='former_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='total_quantity',
            field=models.PositiveIntegerField(default=7),
            preserve_default=False,
        ),
    ]
