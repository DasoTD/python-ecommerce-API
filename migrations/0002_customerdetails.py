# Generated by Django 4.0.4 on 2022-07-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('gmail', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('date', models.TextField(max_length=100)),
            ],
        ),
    ]
