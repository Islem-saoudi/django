# Generated by Django 3.2.14 on 2022-09-09 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_slug_blog_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='slug',
            new_name='slug',
        ),
    ]
