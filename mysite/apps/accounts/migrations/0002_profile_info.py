# Generated by Django 3.0.4 on 2020-04-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='info',
            field=models.TextField(blank=True, verbose_name='Write something about your self'),
        ),
    ]