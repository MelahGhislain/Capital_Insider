# Generated by Django 3.2.5 on 2021-07-27 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailus',
            name='phone_num',
            field=models.CharField(max_length=50),
        ),
    ]