# Generated by Django 4.0.1 on 2022-04-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_quotationitem_pl'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationitem',
            name='hl',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
