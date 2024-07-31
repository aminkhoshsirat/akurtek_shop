# Generated by Django 5.0.7 on 2024-07-31 20:07

import django.core.validators
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_useraddressmodel_position_x_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='birth_date',
            field=django_jalali.db.models.jDateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='city',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='state',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='post_code',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]