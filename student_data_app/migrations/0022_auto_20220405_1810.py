# Generated by Django 3.2.9 on 2022-04-05 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_data_app', '0021_auto_20220405_1803'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentStatus',
        ),
    ]
