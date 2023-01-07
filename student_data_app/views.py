from email import message
from django.shortcuts import render,redirect
from student_data_app.forms import SignUpForm, StudentDetailsForm
from student_data_app.models import Student
from student_data_app.models import StudentStatus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student
from django.contrib.auth import logout

# Create your views here.
def home(request):
    student_list=Student.objects.all()
    return render(request,"home.html",{'students':student_list})

def displaydetails(request,STD_id):
    try:
        displaydetails=StudentStatus.objects.get(id=STD_id)
        return render(request,"showdetails.html",{'display':displaydetails})
    except:
        return redirect('home')

def delete_view(request,id):
    student_list=Student.objects.get(id=id)
    student_list.delete()
    return redirect('home')


def che(request):
    student_list=StudentStatus.objects.all()
    return render(request,"check.html",{'students':student_list})




def create_details_view(request):
    form=StudentDetailsForm()
    if request.method =='POST':
        form=StudentDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'addinfo.html',{'form':form})



def create_view(request):
    if request.method =='POST':
        S_Reg_No=request.POST['S_Reg_No']
        S_Name=request.POST['S_Name']
        S_DOB=request.POST['S_DOB']
        S_Gender=request.POST['S_Gender']
        S_Dept=request.POST['S_Dept']
        S_Yr=request.POST['S_Yr']
        S_Adhar_No=request.POST['S_Adhar_No']
        ins=Student(S_Reg_No= S_Reg_No,S_Name=S_Name,S_DOB=S_DOB,S_Gender=S_Gender,S_Dept=S_Dept, S_Yr= S_Yr,S_Adhar_No=S_Adhar_No)
        ins.save()
        return redirect('add')
    return render(request,'create.html')

def login_user(request):
    if request.method =='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
        else:
            form=AuthenticationForm()
    else:
         form=AuthenticationForm()

    return render(request,'login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')




def register(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})