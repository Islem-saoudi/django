# Generated by Django 3.2.15 on 2022-08-25 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20220818_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
    ]