# Generated by Django 4.1.7 on 2023-04-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('url', models.URLField(blank=True, max_length=255)),
                ('url_to_image', models.URLField(blank=True, max_length=255)),
                ('published_at', models.DateTimeField()),
                ('source_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]