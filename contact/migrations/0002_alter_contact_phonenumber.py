# Generated by Django 4.1.7 on 2023-02-25 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phoneNumber',
            field=models.IntegerField(verbose_name='phoneNumber'),
        ),
    ]