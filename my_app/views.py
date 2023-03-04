from email.message import EmailMessage
import re
from django.shortcuts import render, HttpResponse,redirect
from my_app.forms import TeacherForm
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def Subject(request):
    subject_form = SubjectForm()
    if request.POST:
        sub_name = request.POST['subject_name']
        to_marks = request.POST['total_marks']
        sid = subject.objects.create(subject_name=sub_name,total_marks=to_marks)
        return render(request,"my_app/subject.html",{"subject":subject_form})
    return render(request,"my_app/subject.html",{"subject":subject_form})

@csrf_exempt
def Student(request):
    form = StudentForms(request.POST or None)
    if request.POST:
        # teacher_S = request.POST['Teacher']
        # subject_S = request.POST['Subject']
        if form.is_valid():
            aaa = form.save(commit=False)
            # aaa.Teacher.teacher_name = teacher_S
            # aaa.Subject.subject_name = subject_S
            aaa.save()
        else:
            print(form.errors, "******")               
        return redirect('Change')
    return render(request,"my_app/student.html",{"student":form})
    
@csrf_exempt 
def Teacher(request):
    TeacherF = TeacherForm()
    if request.POST:
        teachers = request.POST['teacher_name']
        print(teachers)
        uid = teacher.objects.create(teacher_name=teachers)
        return render(request,"my_app/teacher.html",{"teacher":TeacherF})
    return render(request,"my_app/teacher.html",{"teacher":teacher})

@csrf_exempt
def Change(request):
    forms = StudentForms()
    all_data = student.objects.all()
    return render(request,"my_app/Edit.html",{'all':all_data})
@csrf_exempt
def delete(request,id):
    get = student.objects.get(pk=id).delete()
    return redirect("Change")
# @csrf_exempt
# def Edit(request,id):
#     get = student.objects.get(pk=id)    
#     form = StudentForms(initial={'student_name': get.student_name,'roll_no':get.roll_no,'Teacher':get.Teacher,'Subject':get.Subject})
#     return render(request,"my_app/Edit_1.html",{'get':get,'form':form})

@csrf_exempt
def UPDATE(request,id):
    instance = student.objects.get(id=id)
    get = student.objects.get(pk=id)   
    form = StudentForms(request.POST or None, instance=instance)
    context = StudentForms(initial={'student_name': get.student_name,'roll_no':get.roll_no,'Teacher':get.Teacher,'Subject':get.Subject})
    if form.is_valid():
        form.save()
        return redirect('Change')
    return render(request, 'my_app/Edit_1.html', {'form': form,'context':context,'get':get})  

