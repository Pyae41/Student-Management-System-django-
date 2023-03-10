from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# from django.http import HttpResponse
# from django.urls import reverse
from .forms import StudentForm
from .models import Student

# Create your views here.
def index(request):
    # get all students 
    students = Student.objects.all()
    
    # add a pagination for students table
    paginator = Paginator(students,5)
    page_number = request.GET.get('page')
    
    try:
        pagi_students = paginator.get_page(page_number) # return a wanted page
    except PageNotAnInteger:
        pagi_students = paginator.page(1) # if page is not a integer then assign the first page
    except EmptyPage:
        pagi_students = paginator.page(paginator.num_pages)

    return render(request,'students/index.html',{'students' : pagi_students})

# adding a new student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'students/add_form.html',{
                'form': StudentForm(),
                'success': True
            })
        
    return render(request,'students/add_form.html',{'form' : StudentForm() })

# update a student's infomation
def edit_student(request,id):
    # get specific student 
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST,student)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request,'students/edit_form.html',{ 'form' : StudentForm(instance=student) })

# delete a student
def del_student(request,id):
    if request.method == 'POST':
        Student.objects.get(id=id).delete()

        return redirect('home')