# Generated by Django 3.0.5 on 2020-05-30 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200530_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='case',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='main.Case'),
        ),
    ]
