# Generated by Django 4.1.1 on 2022-10-02 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publish_date',
            new_name='publish',
        ),
    ]
