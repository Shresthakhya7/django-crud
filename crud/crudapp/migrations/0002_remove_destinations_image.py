# Generated by Django 4.2.16 on 2024-10-27 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinations',
            name='image',
        ),
    ]
