# Generated by Django 3.2.15 on 2022-08-18 12:58

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='FeatureImage',
            field=sorl.thumbnail.fields.ImageField(blank=True, default='default_img.svg', null=True, upload_to='blog/%Y/%m/%d/', verbose_name='Feature Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='FeatureImage',
            field=models.ImageField(blank=True, default='default_img.svg', null=True, upload_to='blog/%Y/%m/%d/'),
        ),
    ]