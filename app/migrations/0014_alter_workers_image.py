# Generated by Django 4.1.1 on 2022-10-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_workers_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='image',
            field=models.ImageField(upload_to='static/workers/'),
        ),
    ]
