# Generated by Django 3.2.9 on 2022-04-03 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_data_app', '0011_alter_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentstatus',
            name='id',
        ),
        migrations.AlterField(
            model_name='studentstatus',
            name='STD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='display', serialize=False, to='student_data_app.student'),
        ),
    ]
