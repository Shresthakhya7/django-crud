# Generated by Django 4.2.16 on 2024-10-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_remove_destinations_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinations',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
