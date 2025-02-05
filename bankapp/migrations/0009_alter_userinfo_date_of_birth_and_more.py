# Generated by Django 5.1 on 2025-01-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0008_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='full_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='identity_type',
            field=models.CharField(blank=True, choices=[('national_id_card', 'National ID Card'), ('drivers_license', 'Drivers License'), ('international_passport', 'International Passport')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='kin_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lga',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='marital',
            field=models.CharField(blank=True, choices=[('married', 'Married'), ('single', 'Single'), ('other', 'Other')], max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='next_of_kin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='passport',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='residential_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='sign/'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='state',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
