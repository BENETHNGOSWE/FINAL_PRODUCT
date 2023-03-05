from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Course, Masomo, Question
from .forms import QuestionForm


# Create your views here.


# def home(request):
#     return render(request, 'FYPAPP/home.html')
#     # return render(request,'teacher/teacher_dashboard.html'

# def dashboard(request):
#     return render(request, 'FYPAPP/dashboard.html')

# def add_question(request):
#     # return render(request, 'FYPAPP/add_question.html')
#     ainayaswali= Question.objects.all()
      
#     if request.method == 'POST':
#         somo = request.POST.get('somo')
#         topic = request.POST.get('topic')
#         questiontype = request.POST.get('questiontype')
#         questionLevel = request.POST.get('questionLevel')
#         questionText = request.POST.get('questionText')

#         new_question = Question(
#             somo=somo,
#             topic=topic,
#             questiontype=questiontype,
#             questionLevel=questionLevel,
#             questionText=questionText
#         )
#         new_question.save()
#     return render(request, 'FYPAPP/add_question.html', {"questiontype":ainayaswali})

# def question(request):
#     ainayaswali = QuestionType.objects.all()
#     return render(request, 'FYPAPP/add_question.html', {"questiontype":ainayaswali})


# def question_level(request):
#     datamaswalilevel = QuestionLevel.objects.all()
#     return render(request, 'FYPAPP/add_question.html', {"questionlevel":datamaswalilevel})



def add_course(request):
    data = Course.objects.all()
    # print(data)
    if request.method == 'POST':
        coursename = request.POST['coursename']
        coursecode = request.POST['coursecode']
        

        new_course = Course(courseName=coursename, courseCode=coursecode)
        new_course.save()
    return render(request, 'FYPAPP/add_course.html', {"course":data})
    


def add_module(request):
    # if request.method == 'POST':
    #     form = MasomoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # return render(request, 'FYPAPP/add_module.html', {'form':form})

    #     else:
    #         form = MasomoForm()
    #         return render(request, 'FYPAPP/add_module.html', {'form':form})    
    datamasomo = Masomo.objects.all()
    if request.method == 'POST':
        modulename = request.POST.get('modulename')
        modulecode = request.POST.get('modulecode')
        course = request.POST.get('course')

        new_module = Masomo(moduleName=modulename, moduleCode=modulecode, course=course)
        new_module.save()
    return render(request, 'FYPAPP/add_module.html', {"masomo":datamasomo})

# def add_question(request):
#     datamaswali = Question.objects.all()
#     if request.method == 'POST':
#         somo = request.POST.get('somo')
#         topic = request.POST.get('topic')
#         questiontype = request.POST.get('questiontype')
#         questionLevel = request.POST.get('questionLevel')  
#         questionText = request.POST.get('questionText')

#         new_question = Question(
#             somo=somo,
#             topic=topic,
#             quesiontype=questiontype,
#             questionLevel=questionLevel,
#             questionText=questionText
#         )
#         new_question.save()
#     return render(request, 'FYPAPP/add_question.html', {"maswali":datamaswali})
        



class home(TemplateView):
    template_name = 'FYPAPP/home.html'


class dashboard(TemplateView):
    template_name = 'FYPAPP/dashboard.html'

# class add_question(TemplateView):
#     template_name = 'FYPAPP/add_question.html'
    

    

# def add_question(request):
#     # datacourse = Question.objects.all()
#     context = {'add_question':Question.objects.all()}
#     return render(request, 'FYPAPP/add_question.html', context)      

# def data_read(request):
#     context = {'add_question': Question.objects.all()}
#     return render(request, "FYPAPP/add_question.html", context)



# def manage_question(request):
#     if request.method == "POST":
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/managequestion')  

#     else:
#             form = QuestionForm()
#             return render(request, "FYPAPP/manage_question.html", {"form":form})  
# # def question(request):
#     if request.method == "POST":
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/data') 

#     else:
#         form = QuestionForm()
#         return render(request, 'FYPAPP/add_question.html', {'form':form})           


def question_manage(request):
    context = {'question_manage': Question.objects.all()}
    return render(request, "FYPAPP/question_manage.html", context)
# def question_manage(request):
#     context = {'data_read': Question.objects.all()}
#     return render(request, "FYPAPP/data_read.html", context)


def add_maswali(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('/data')  

    else:
            form = QuestionForm()
            return render(request, "FYPAPP/add_question.html", {"form":form})  

# def question_manage(request):
#     context = {'data_read': Question.objects.all()}
#     return render(request, "FYPAPP/data_read.html", context)



# def add_question(request):
#     if request.method == "POST":
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/data')  

#     else:
#             form = QuestionForm()
#             return render(request, "FYPAPP/data_form.html", {"form":form})  





def data_read(request):
    context = {'data_read': Question.objects.all()}
    return render(request, "data_read.html", context)



def data_form(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/data')  

    else:
            form = QuestionForm()
            return render(request, "data_form.html", {"form":form})  