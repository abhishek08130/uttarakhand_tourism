# Generated by Django 4.0.6 on 2022-11-12 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_place_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image2',
            field=models.URLField(blank=True, null=True),
        ),
    ]