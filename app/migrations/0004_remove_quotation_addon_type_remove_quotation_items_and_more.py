# Generated by Django 4.0.1 on 2022-02-26 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_addon_nos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='addon_type',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='items',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='Quotation',
        ),
    ]
