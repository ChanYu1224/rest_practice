# Generated by Django 3.2.7 on 2021-09-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
