# Generated by Django 2.2.1 on 2019-05-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20190516_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
