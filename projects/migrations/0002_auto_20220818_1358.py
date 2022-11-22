# Generated by Django 3.2.15 on 2022-08-18 12:58

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='SlugProject',
        ),
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='Name', verbose_name='slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projects',
            name='Description',
            field=models.CharField(max_length=300, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='Name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
