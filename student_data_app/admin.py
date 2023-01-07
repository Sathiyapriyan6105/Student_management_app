from django.contrib import admin
from student_data_app.models import Student
from student_data_app.models import StudentStatus
#Register your models here.
# class StudentAdmin(admin.ModelAdmin):
#     list_display=['S_Reg_No','S_Name','S_DOB','S_Gender','S_Dept',' S_Yr','S_Adhar_No']
#     search_fields=['S_Name']
#     list_per_page=8

# class StudentDetailAdmin(admin.ModelAdmin):
#     list=['S_Name',' S_Attendance','S_Percentag']

admin.site.register(Student)
admin.site.register(StudentStatus)