# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0006_message_reference_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='reference_id',
        ),
    ]
