# Generated by Django 5.1 on 2024-09-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyst', '0008_remove_organization_projects_delete_project'),
        ('projects', '0003_remove_project_organizations'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='projects',
            field=models.ManyToManyField(to='projects.project'),
        ),
    ]
