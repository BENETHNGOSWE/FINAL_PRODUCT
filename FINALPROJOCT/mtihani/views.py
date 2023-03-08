from django.shortcuts import render, redirect
from .models import Exam
from .forms import ExamForm

# Create your views here.
# def exam_manage(request):
#     context = {'exam_manage': Exam.objects.all()}
#     return render(request, "mtihani/exam_manage.html", context)

# def add_exam(request):
#     if request.method == "POST":
#         form = ExamForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/exam')

#     else:
#             form = ExamForm()
#             return render(request, "mtihani/add_exam.html", {"form":form})        

def exam_manage(request):
    context = {'exam_manage': Exam.objects.all()}
    return render(request, "mtihani/exam_manage.html", context)

def add_exam(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('/exam')  

    else:
            form = ExamForm()
            return render(request, "mtihani/add_exam.html", {"form":form})         
