# Generated by Django 4.0.6 on 2022-07-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]