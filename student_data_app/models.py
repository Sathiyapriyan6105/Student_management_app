from datetime import datetime
from distutils.command.upload import upload
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


#Create your models here.
class Student(models.Model):

    GENDER= (
        ('M','M'),
        ('F','F'),
    )

    DEPT=(
        ('MECH','MECH'),
        ('CIVIL','CIVIL'),
        ('CSE','CSE'),
        ('EEE','EEE'),
    )
    YEAR=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
    )

    id = models.AutoField(primary_key=True)
    S_Reg_No=models.IntegerField(null=True)
    S_Name=models.CharField(max_length=100,null=True)
    S_DOB=models.DateField(null=True)
    S_Gender=models.CharField(max_length=100,null=True,choices=GENDER)
    S_Dept=models.CharField(max_length=100,null=True,choices=DEPT)
    S_Yr=models.CharField(max_length=100,null=True,choices=YEAR)
    S_Adhar_No=models.IntegerField(null=True)

    def __str__(self):
        return self.S_Name

class StudentStatus(models.Model):

    S_Name=models.CharField(max_length=100,null=True)
    S_Attendance=models.IntegerField(null=True)
    S_Percentage=models.IntegerField(null=True)
    STD=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="display",)

    def __str__(self):
        return self.S_Name

