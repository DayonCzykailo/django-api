# Generated by Django 5.1.3 on 2024-11-18 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_django_api_rest', '0002_rename_estudant_estudent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estudent',
            new_name='Student',
        ),
    ]
