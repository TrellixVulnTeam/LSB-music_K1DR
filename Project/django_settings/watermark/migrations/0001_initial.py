# Generated by Django 2.0.5 on 2018-05-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('srcLink', models.CharField(blank=True, max_length=200, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'watermark_song',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=100)),
                ('songs', models.ManyToManyField(to='watermark.Song')),
            ],
        ),
    ]
