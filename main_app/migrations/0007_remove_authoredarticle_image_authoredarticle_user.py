# Generated by Django 4.1.7 on 2023-04-26 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_authoredarticle_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authoredarticle',
            name='image',
        ),
        migrations.AddField(
            model_name='authoredarticle',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]