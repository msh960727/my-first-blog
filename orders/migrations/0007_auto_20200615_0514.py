# Generated by Django 3.0.4 on 2020-06-14 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200614_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pass_word',
            field=models.IntegerField(default=8809),
        ),
    ]