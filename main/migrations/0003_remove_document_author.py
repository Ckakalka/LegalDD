# Generated by Django 3.0.5 on 2020-05-21 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200521_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='author',
        ),
    ]
