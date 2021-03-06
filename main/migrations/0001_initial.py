# Generated by Django 3.0.1 on 2020-01-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('urlToImg', models.CharField(max_length=200)),
                ('publishedAt', models.DateTimeField(verbose_name='Date Published')),
                ('content', models.TextField()),
            ],
        ),
    ]
