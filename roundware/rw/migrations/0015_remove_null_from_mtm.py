# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-20 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rw', '0014__data__speaker_shape_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='loc_description',
            field=models.ManyToManyField(blank=True, to='rw.LocalizedString'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='tags',
            field=models.ManyToManyField(blank=True, to='rw.Tag'),
        ),
        migrations.AlterField(
            model_name='masterui',
            name='header_text_loc',
            field=models.ManyToManyField(blank=True, to='rw.LocalizedString'),
        ),
        migrations.AlterField(
            model_name='project',
            name='demo_stream_message_loc',
            field=models.ManyToManyField(blank=True, related_name='demo_stream_msg_string', to='rw.LocalizedString'),
        ),
        migrations.AlterField(
            model_name='project',
            name='legal_agreement_loc',
            field=models.ManyToManyField(blank=True, related_name='legal_agreement_string', to='rw.LocalizedString'),
        ),
        migrations.AlterField(
            model_name='project',
            name='out_of_range_message_loc',
            field=models.ManyToManyField(blank=True, related_name='out_of_range_msg_string', to='rw.LocalizedString'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sharing_message_loc',
            field=models.ManyToManyField(blank=True, related_name='sharing_msg_string', to='rw.LocalizedString'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='loc_description',
            field=models.ManyToManyField(blank=True, related_name='tag_desc', to='rw.LocalizedString'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='loc_msg',
            field=models.ManyToManyField(blank=True, to='rw.LocalizedString'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='relationships',
            field=models.ManyToManyField(blank=True, related_name='_tag_relationships_+', to='rw.Tag'),
        ),
    ]
