# Generated by Django 2.2.7 on 2019-11-22 09:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('writer', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
            ],
        ),
    ]
