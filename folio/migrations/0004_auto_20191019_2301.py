# Generated by Django 2.2.6 on 2019-10-19 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0003_auto_20191019_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='cv',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
