
from django import forms
from student_data_app.models import StudentStatus
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class StudentDetailsForm(forms.ModelForm):
     class Meta:
        model=StudentStatus
        fields='__all__'


class SignUpForm(UserCreationForm):
   # def __init__(self, *args, **kwargs):
   #     super().__init__(*args, **kwargs)
   #     self.fields["username"].widget.attrs.update
   class Meta:
      model=User
      fields=['username','password1','password2']
