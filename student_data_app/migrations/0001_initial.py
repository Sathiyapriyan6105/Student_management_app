# Generated by Django 3.2.9 on 2022-03-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ID_NO', models.IntegerField(primary_key=b'I01\n', serialize=False)),
                ('S_Reg_No', models.IntegerField(max_length=12)),
                ('S_Name', models.CharField(max_length=100)),
                ('S_DOB', models.DateField()),
                ('S_Gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=100, null=True)),
                ('S_Dept', models.CharField(max_length=10)),
                ('S_Adhar_No', models.IntegerField(max_length=12)),
            ],
        ),
    ]
