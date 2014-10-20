# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(max_length=64, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='big',
            field=models.ImageField(editable=False, default='', upload_to='1080p/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='layer',
            field=models.CharField(max_length=256, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='original',
            field=models.ImageField(default='', upload_to='original/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(editable=False, default='', upload_to='thumbnail/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=64, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='album',
            field=models.ForeignKey(null=True, to='gallery.Album'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(editable=False, upload_to='regular/'),
        ),
    ]
