# Generated by Django 2.0.7 on 2018-07-19 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_usersiterole'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersiterole',
            old_name='role',
            new_name='name',
        ),
    ]
