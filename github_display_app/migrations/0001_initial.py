# Generated by Django 3.0 on 2019-12-18 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repository_ID', models.CharField(max_length=2000)),
                ('name', models.CharField(blank=True, max_length=2000, null=True)),
                ('url', models.CharField(blank=True, max_length=2000, null=True)),
                ('created_date', models.DateTimeField()),
                ('last_push_date', models.DateTimeField()),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('stars', models.PositiveIntegerField()),
            ],
        ),
    ]
