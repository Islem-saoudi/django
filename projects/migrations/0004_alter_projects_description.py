# Generated by Django 3.2.15 on 2022-10-03 10:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_projects_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='Description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
