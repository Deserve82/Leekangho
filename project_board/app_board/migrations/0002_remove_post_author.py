# Generated by Django 2.2.7 on 2019-11-11 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
