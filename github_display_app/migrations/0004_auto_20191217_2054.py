# Generated by Django 3.0 on 2019-12-18 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_display_app', '0003_auto_20191217_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubrecord',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='githubrecord',
            name='name',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='githubrecord',
            name='url',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
