# Generated by Django 3.2.9 on 2022-04-01 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_data_app', '0004_alter_studentstatus_std'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentstatus',
            name='STD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_data_app.student'),
        ),
    ]
