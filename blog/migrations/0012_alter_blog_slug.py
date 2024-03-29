# Generated by Django 3.2.15 on 2022-09-14 00:17

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20220913_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='Title', unique_with=('CreatedDate__month',)),
        ),
    ]
