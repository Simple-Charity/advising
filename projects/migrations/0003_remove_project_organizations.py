# Generated by Django 5.1 on 2024-09-12 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_organizations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='organizations',
        ),
    ]
