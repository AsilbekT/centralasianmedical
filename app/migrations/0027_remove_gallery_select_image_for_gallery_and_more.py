# Generated by Django 4.1.1 on 2022-12-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='select_image_for_gallery',
        ),
        migrations.AddField(
            model_name='gallery',
            name='select_image_for_gallery',
            field=models.ImageField(default='static/db/gallery/', upload_to='static/db/gallery/'),
        ),
    ]
