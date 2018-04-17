# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-17 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basemodule',
            options={'ordering': ['title'], 'verbose_name': 'Module', 'verbose_name_plural': 'Modules'},
        ),
        migrations.AddField(
            model_name='basemodule',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_cms.basemodule_set+', to='contenttypes.ContentType'),
        ),
    ]
