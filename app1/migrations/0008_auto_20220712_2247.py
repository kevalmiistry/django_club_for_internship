# Generated by Django 3.0 on 2022-07-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20220712_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendoracc',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
