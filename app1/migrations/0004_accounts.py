# Generated by Django 3.0 on 2022-07-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_author_blog_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('birth', models.DateField()),
            ],
        ),
    ]
