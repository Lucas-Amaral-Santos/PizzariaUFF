# Generated by Django 2.2.5 on 2019-10-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0007_remove_produto_data_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='data_cadastro',
            field=models.DateField(null=True),
        ),
    ]