# Generated by Django 4.1.1 on 2022-10-04 16:49

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_workers_event_in_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='about',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workers',
            name='number',
            field=models.CharField(default='', max_length=200),
        ),
    ]
