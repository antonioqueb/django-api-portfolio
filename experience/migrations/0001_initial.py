# Generated by Django 4.1.7 on 2023-02-25 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=80)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('logoUrl', models.ImageField(upload_to='logos/')),
            ],
            options={
                'verbose_name_plural': 'Experience',
            },
        ),
    ]
