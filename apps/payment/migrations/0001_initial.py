# Generated by Django 5.0.7 on 2024-07-31 17:05

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BucketProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.PositiveIntegerField(blank=True, null=True)),
                ('number', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='BuketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
                ('transaction_code', models.CharField(blank=True, max_length=100, null=True)),
                ('paid_date', django_jalali.db.models.jDateTimeField(blank=True, null=True)),
                ('price_paid', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(blank=True, max_length=1000, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('bailee_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('bailee_phone', models.CharField(blank=True, max_length=11, null=True)),
                ('transaction_mode', models.CharField(blank=True, max_length=1000, null=True)),
                ('post_price', models.PositiveIntegerField(default=0)),
                ('delivery_date', django_jalali.db.models.jDateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WalletModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('last_charge', django_jalali.db.models.jDateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WalletTransactionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('deposit', 'deposit'), ('endurance', 'endurance')], max_length=500)),
                ('description', models.TextField()),
                ('date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
            ],
        ),
    ]
