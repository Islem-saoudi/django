# Generated by Django 3.2.15 on 2022-08-19 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_authorid_blog_authorid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='authorId',
            new_name='AuthorId',
        ),
    ]
