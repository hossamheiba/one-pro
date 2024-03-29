# Generated by Django 5.0.2 on 2024-02-22 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cateogry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(default='des', max_length=1000)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('vacancy', models.IntegerField(default=1)),
                ('job_type', models.CharField(choices=[('full time', 'full time'), ('part time', 'part time')], max_length=100)),
                ('salary', models.IntegerField(default=0)),
                ('experienc', models.IntegerField(default=1)),
                ('cateogry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.cateogry')),
            ],
            options={
                'verbose_name': 'home',
                'verbose_name_plural': 'home',
            },
        ),
    ]
