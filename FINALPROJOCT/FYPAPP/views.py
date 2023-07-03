from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Course, Masomo,QuestionChoice,QuestionShortterm, Department, QuestionLongTerm
from .forms import  CourseForm, MasomoForm, QuestionChoiceForm, QuestionShorttermForm, QuestionForm, DepartmentForm
from django.db import connection
from django.contrib.auth.decorators import login_required
from mtihani.models import Mtihani
# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'FYPAPP/dashboard.html')

   

# def dashboard(request):
#     return render(request, 'FYPAPP/dashboard.html')

# @login_required
def course_manage(request):
    context = {'course':  Course.objects.all()}
    return render(request, 'FYPAPP/course_manage.html', context)
    
def total(request):
    courses = Masomo.objects.all()
    totalcourse = courses.count()
    print(totalcourse)
    context = {'courses':courses, 'totalcourse':totalcourse}
    return render(request, 'FYPAPP/course_manage.html', context)
#************************COURSE MANAGEMENT*****************************
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/coursedata')   

    else:
        form = CourseForm()
        return render(request, 'FYPAPP/add_course.html', {"form":form})    
         
def update_course(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/coursedata')

    context = {"form":form}
    return render(request, 'FYPAPP/add_course.html', context)

def delete_course(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect('/coursedata')

# *************************DEPARTMENT********************************
def dept_manage(request):
    context = {'dept':  Department.objects.all()}
    return render(request, 'FYPAPP/dept_manage.html', context)
    


def add_dept(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/deptdata')   

    else:
        form = DepartmentForm()
        return render(request, 'FYPAPP/add_dept.html', {"form":form})    
         


def update_dept(request, pk):
    deptm = Department.objects.get(id=pk)
    form = DepartmentForm(instance=deptm)

    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=deptm)
        if form.is_valid():
            form.save()
            return redirect('/deptdata')

    context = {"form":form}
    return render(request, 'FYPAPP/add_dept.html', context)


def delete_dept(request, pk):
    dept = Department.objects.get(id=pk)
    dept.delete()
    return redirect('/deptdata')


# *******************************************************************
#*********************MODULE MANAGEMENT******************************
def module_manage(request):
    context = {'module_manage': Masomo.objects.all()}
    return render(request, 'FYPAPP/module_manage.html', context)


def add_module(request):
    if request.method == "POST":
        form = MasomoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/moduledata')

    else:
         form = MasomoForm()
         return render(request, 'FYPAPP/add_module.html', {"form":form})           



def update_module(request, pk):
    masomo = Masomo.objects.get(id=pk)
    form = MasomoForm(instance=masomo)

    if request.method == "POST":
        form = MasomoForm(request.POST, instance=masomo)
        if form.is_valid():
            form.save()
            return redirect('/moduledata')

    context = {"form":form}
    return render(request, 'FYPAPP/add_module.html', context)  


def delete_module(request, pk):
    masomo = Masomo.objects.get(id=pk)
    masomo.delete()
    return redirect('/moduledata')
# ********************************************************************************* 

# ****************************************************************************


def question_long_manage(request):
    context = {'question_long': QuestionLongTerm.objects.all()}
    return render(request, "FYPAPP/question_long_manage.html", context)

def question_choice_manage(request):
    context = {'question_choice': QuestionChoice.objects.all()}
    return render(request, "FYPAPP/question_choice_manage.html", context)

def question_short_manage(request):
    context = {'question_manage': QuestionShortterm.objects.all()}
    return render(request, "FYPAPP/question_manage.html", context)

# ***************************ADD QUESTIONS HAPA ***************************************

@login_required
def add_question_long(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user  # Associate the question with the logged-in user
            question.save()
            return redirect('/long')  
    else:
        form = QuestionForm()
    return render(request, "FYPAPP/add_question.html", {"form": form})

@login_required
def add_question_choice(request):
    if request.method == "POST":
        form = QuestionChoiceForm(request.POST)
        if form.is_valid():
            question_choice = form.save(commit=False)
            question_choice.user = request.user  # Associate the question choice with the logged-in user
            question_choice.save()
            return redirect('/choice')
    else:
        form = QuestionChoiceForm()
    return render(request, "FYPAPP/add_question_choice.html", {'form': form})    

@login_required
def add_question_short(request):
    if request.method == "POST":
        form = QuestionShorttermForm(request.POST)
        if form.is_valid():
            question_shortterm = form.save(commit=False)
            question_shortterm.user = request.user  # Associate the short-term question with the logged-in user
            question_shortterm.save()
            return redirect('/short')
    else:
        form = QuestionShorttermForm()
    return render(request, "FYPAPP/add_question.html", {"form": form})       
# *****************************UPDATE QUESTION******************************************************************

def update_question_long(request, pk):
    question = QuestionLongTerm.objects.get(id=pk)
    form = QuestionForm(instance=question)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("/long")

    context = {"form": form }
    return render(request, 'FYPAPP/add_question.html', context)

def update_question_short(request,pk):
    question = QuestionShortterm.objects.get(id=pk)
    form = QuestionShorttermForm(instance=question)

    if request.method == "POST":
        form = QuestionShorttermForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
        return redirect('/short')    

    context = {'form':form}
    return render(request, 'FYPAPP/add_question.html', context)            

def update_question_choice(request, pk):
    question = QuestionChoice.objects.get(id=pk)
    form = QuestionChoiceForm(instance=question)

    if request.method == "POST":
        form = QuestionChoiceForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
        return redirect('/choice')

    context = {'form':form}
    return render(request, 'FYPAPP/add_question_choice.html', context)


#***************************************************************** 
# ********************DELETE QUESTION*****************************
        
def delete_question_long(request, pk):
   long = QuestionLongTerm.objects.get(id=pk)
   long.delete()
   return redirect('/long')


def delete_question_short(request, pk):
    short = QuestionShortterm.objects.get(id=pk)
    short.delete()
    return redirect('/short')


def delete_question_choice(request, pk):
    choice = QuestionChoice.objects.get(id=pk)
    choice.delete()
    return redirect('/choice')
#   ****************************************************************








def display(request):
    category = QuestionChoice.objects.filter(category_id=1).only('question')
    print(category)
    print(connection.queries)
    return render(request, "FYPAPP/add_question_choice.html", {'category':category})        



# class home(TemplateView):
#     template_name = 'FYPAPP/home.html'


# class dashboard(TemplateView):
#     template_name = 'FYPAPP/dashboard.html'
  


    



