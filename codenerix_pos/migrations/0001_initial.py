# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-21 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('codenerix_payments', '0018_auto_20170303_0839'),
        ('codenerix_invoicing', '0021_auto_20170531_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='POS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('services', models.CharField(max_length=250, unique=True, verbose_name='Services')),
                ('cid', models.CharField(max_length=250, unique=True, verbose_name='CID')),
                ('key', models.CharField(max_length=250, unique=True, verbose_name='KEY')),
                ('payments', models.ManyToManyField(related_name='pos', to='codenerix_payments.PaymentRequest')),
            ],
            options={
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
            },
        ),
        migrations.CreateModel(
            name='POSSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('pos_x', models.IntegerField(verbose_name='Pos X')),
                ('pos_y', models.IntegerField(verbose_name='Pos Y')),
                ('orders', models.ManyToManyField(related_name='slots', to='codenerix_invoicing.SalesOrder')),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='codenerix_pos.POS')),
            ],
            options={
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
            },
        ),
    ]
