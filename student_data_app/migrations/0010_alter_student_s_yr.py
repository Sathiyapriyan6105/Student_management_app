# Generated by Django 3.2.9 on 2022-04-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_data_app', '0009_student_studentstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='S_Yr',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100, null=True),
        ),
    ]
