# Generated by Django 4.0.6 on 2022-08-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(null=True, upload_to='avatar/', verbose_name='Avatar'),
        ),
    ]
