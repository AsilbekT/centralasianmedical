# Generated by Django 4.1.1 on 2022-10-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='static/news/')),
            ],
        ),
    ]
