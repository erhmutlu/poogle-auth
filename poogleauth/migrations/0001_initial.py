# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import poogleauth.managers.user


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=20, verbose_name=b'username')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'email')),
                ('first_name', models.CharField(max_length=30, verbose_name=b'first name')),
                ('last_name', models.CharField(max_length=30, verbose_name=b'last name')),
                ('gender', models.IntegerField(null=True, verbose_name=b'gender', choices=[(1, b'MALE'), (2, b'FEMALE')])),
                ('age', models.IntegerField(null=True, verbose_name=b'age')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'poogleauth_user',
            },
            managers=[
                ('objects', poogleauth.managers.user.UserManager()),
            ],
        ),
    ]
