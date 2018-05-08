# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-19 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_pos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pos',
            name='hardware',
            field=models.ManyToManyField(related_name='poss', to='codenerix_pos.POSHardware', verbose_name='Hardware'),
        ),
        migrations.AlterField(
            model_name='pos',
            name='payments',
            field=models.ManyToManyField(related_name='poss', to='codenerix_payments.PaymentRequest', verbose_name='Payments'),
        ),
        migrations.AlterField(
            model_name='pos',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poss', to='codenerix_pos.POSZone', verbose_name='Zone'),
        ),
        migrations.AlterField(
            model_name='poshardware',
            name='pos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hardwares', to='codenerix_pos.POS', verbose_name='Hardware'),
        ),
        migrations.AlterField(
            model_name='posslot',
            name='orders',
            field=models.ManyToManyField(editable=False, related_name='slots', to='codenerix_invoicing.SalesOrder', verbose_name='Orders'),
        ),
        migrations.AlterField(
            model_name='posslot',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='codenerix_pos.POSZone', verbose_name='Zone'),
        ),
    ]