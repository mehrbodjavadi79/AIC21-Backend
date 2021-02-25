# Generated by Django 3.1.5 on 2021-02-25 08:28

from django.db import migrations
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0006_lobbyqueue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='id',
            field=model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
