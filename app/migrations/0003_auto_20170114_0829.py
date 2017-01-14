# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170114_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.RemoveField(
            model_name='question',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='question',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='Choice1',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='Choice2',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='Choice3',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='Choice4',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='Choice5',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='Question',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
    ]
