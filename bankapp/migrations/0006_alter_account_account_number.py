# Generated by Django 5.1 on 2025-01-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_remove_account_account_id_remove_account_red_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(max_length=10, null=True, unique=True),
        ),
    ]
