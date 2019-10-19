# Generated by Django 2.2.6 on 2019-10-19 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_one', models.TextField(blank=True)),
                ('desc_two', models.TextField(blank=True)),
                ('desc_three', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSaid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('quote', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LanguageSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('percent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=210)),
                ('desc', models.TextField()),
                ('awesome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('text_desc', models.TextField()),
                ('cv', models.CharField(blank=True, max_length=200)),
                ('resume', models.CharField(blank=True, max_length=200)),
                ('git', models.CharField(blank=True, max_length=200)),
                ('linked_in', models.CharField(blank=True, max_length=200)),
                ('face', models.CharField(blank=True, max_length=200)),
                ('tweeter', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('link', models.URLField(unique=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
