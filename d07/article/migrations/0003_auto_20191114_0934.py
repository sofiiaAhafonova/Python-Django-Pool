# Generated by Django 2.2.7 on 2019-11-14 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20191113_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlemodel',
            options={'ordering': ['-created']},
        ),
    ]
