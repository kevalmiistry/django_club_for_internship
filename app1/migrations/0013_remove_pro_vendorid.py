# Generated by Django 3.0 on 2022-07-12 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20220712_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pro',
            name='vendorid',
        ),
    ]
