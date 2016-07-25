# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 04:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0001_initial'),
        ('executions', '0003_auto_20160723_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutionTC',
            fields=[
                ('exec_tc_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('P', 'Pass'), ('F', 'Fail'), ('N', 'No Run'), ('S', 'Skip')], default='N', max_length=1)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='execution',
            name='status',
        ),
        migrations.RemoveField(
            model_name='execution',
            name='tc_id',
        ),
        migrations.AddField(
            model_name='execution',
            name='env',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='executiontc',
            name='exec_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executions.Execution'),
        ),
        migrations.AddField(
            model_name='executiontc',
            name='tc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testcases.TestCase'),
        ),
    ]
