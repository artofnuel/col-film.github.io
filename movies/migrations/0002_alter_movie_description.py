# Generated by Django 4.0.6 on 2022-08-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
