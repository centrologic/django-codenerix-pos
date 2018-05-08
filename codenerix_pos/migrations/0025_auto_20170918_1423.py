# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-18 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_pos', '0024_auto_20170825_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posoperator',
            name='pos',
        ),
        migrations.AddField(
            model_name='posoperator',
            name='pos',
            field=models.ManyToManyField(related_name='pos_operators', to='codenerix_pos.POS', verbose_name='POS'),
        ),
    ]