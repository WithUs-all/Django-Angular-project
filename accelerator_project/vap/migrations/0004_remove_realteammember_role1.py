# Generated by Django 3.0.2 on 2020-01-28 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vap', '0003_realteammember_role1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realteammember',
            name='role1',
        ),
    ]
