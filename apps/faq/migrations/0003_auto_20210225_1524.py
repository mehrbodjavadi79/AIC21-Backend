# Generated by Django 3.1.5 on 2021-02-25 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20200202_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='questionwithanswer',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='faq.questiontitle'),
        ),
    ]
