# Generated by Django 5.1 on 2025-01-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0009_alter_userinfo_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='kin_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
