# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20141019_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='image',
            name='big',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='layer',
        ),
        migrations.RemoveField(
            model_name='image',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='image',
            name='album',
            field=models.ForeignKey(to='gallery.Album'),
        ),
    ]
