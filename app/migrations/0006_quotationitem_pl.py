# Generated by Django 4.0.1 on 2022-04-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_product_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationitem',
            name='pl',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
