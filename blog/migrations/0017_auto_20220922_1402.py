# Generated by Django 3.2.15 on 2022-09-22 14:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_rename_content_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='Content',
            field=ckeditor.fields.RichTextField(default=22),
            preserve_default=False,
        ),
    ]