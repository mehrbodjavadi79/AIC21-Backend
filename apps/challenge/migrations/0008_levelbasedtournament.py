# Generated by Django 3.1.5 on 2021-02-25 08:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0007_auto_20210225_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelBasedTournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('size', models.PositiveSmallIntegerField(default=8)),
                ('tournament', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='level_based_tournament', to='challenge.tournament')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
