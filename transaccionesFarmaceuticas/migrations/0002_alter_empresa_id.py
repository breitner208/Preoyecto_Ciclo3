# Generated by Django 4.1 on 2022-09-15 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaccionesFarmaceuticas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
