# Generated by Django 5.0.7 on 2024-07-31 17:05

import django.core.validators
import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('fullname', models.CharField(default='No Name', max_length=150)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.customuser')),
                ('ban', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='user/profiles')),
                ('register_date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('post_code', models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('user.customuser',),
        ),
        migrations.CreateModel(
            name='UserAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=1000)),
                ('address', models.TextField()),
                ('plaque', models.IntegerField()),
                ('post_code', models.CharField(max_length=10)),
                ('position_x', models.FloatField()),
                ('position_y', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
