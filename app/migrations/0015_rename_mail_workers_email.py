# Generated by Django 4.1.1 on 2022-10-04 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_workers_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workers',
            old_name='mail',
            new_name='email',
        ),
    ]
