# Generated by Django 4.1.1 on 2022-12-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_course_course_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
