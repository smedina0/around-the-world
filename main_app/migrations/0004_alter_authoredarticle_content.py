# Generated by Django 4.1.7 on 2023-04-22 19:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_authoredarticle_facebook_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authoredarticle',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]