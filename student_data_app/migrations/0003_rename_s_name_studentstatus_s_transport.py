# Generated by Django 3.2.9 on 2022-04-01 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_data_app', '0002_auto_20220401_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentstatus',
            old_name='S_Name',
            new_name='S_Transport',
        ),
    ]