# Generated by Django 2.2.17 on 2021-02-06 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20210206_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Category'),
        ),
    ]
