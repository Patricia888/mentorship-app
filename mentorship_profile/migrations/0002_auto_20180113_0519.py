# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 05:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='repo_url',
            new_name='projects_url',
        ),
    ]
