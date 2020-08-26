# Generated by Django 3.0.7 on 2020-07-09 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Pub Date')),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Pub Date')),
                ('cover', models.ImageField(default='static/images/UOB.png', upload_to='static/images/post', verbose_name='Blog Cover')),
                ('views', models.IntegerField(default=0, verbose_name='Viewed Number')),
                ('recommend', models.BooleanField(default=False, verbose_name='Recommend Blog')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
