# Generated by Django 4.1.7 on 2023-04-23 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='authoredarticle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article_images/'),
        ),
    ]