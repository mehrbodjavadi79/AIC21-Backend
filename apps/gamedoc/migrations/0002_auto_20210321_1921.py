# Generated by Django 3.1.5 on 2021-03-21 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamedoc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamedoc',
            name='repo_name',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='gamedoc',
            name='user_name',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
