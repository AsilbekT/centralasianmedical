# Generated by Django 4.1.1 on 2022-10-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_workers_facebook_workers_instagram_workers_telegram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/db/gallery/')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='static/db/news/'),
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(upload_to='static/db/news/'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='image',
            field=models.ImageField(upload_to='static/db/workers/'),
        ),
    ]
