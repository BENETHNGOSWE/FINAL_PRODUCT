from django.urls import path
from . import views
from FYPAPP import views

app_name = 'FYPAPP'

urlpatterns = [
    # path('', views.home.as_view(), name='homepage'),
    path('', views.dashboard, name='dashboard'),


    path('addcourse/', views.add_course, name='add_course'),
    path('display/', views.display, name='display'),

    path('coursedata/', views.course_manage, name='course_manage'),
    path('updatecourse/<str:pk>/', views.update_course, name="update_course"),
    path('deletecourse/<str:pk>/', views.delete_course, name="delete_course"),

    path('addmodule/', views.add_module, name='add_module'),
    path('moduledata/', views.module_manage, name='module_manage'),
    path('updatemodule/<str:pk>/', views.update_module, name="update_module"), 
    path('deletemodule/<str:pk>/', views.delete_module, name="delete_module"),

    path('long/', views.question_long_manage, name="question_long_manage"),
    path('choice/', views.question_choice_manage, name="question_choice_manage"),
    path('short/',views.question_short_manage, name="question_short_manage"),
    # path('updatemodule/', views.update_module, name="update_module"),
   
    path('adddept/', views.add_dept, name='add_dept'),
    path('deptdata/', views.dept_manage, name='dept_manage'),
    path('updatedept/<str:pk>/', views.update_dept, name="update_dept"),
    path('deletedept/<str:pk>/', views.delete_dept, name="delete_dept"),

    # path('questioncount/', views.question_count, name='question_count'),

    path('addquestion/', views.add_question_long, name="add_question"),
    path('addquestionchoice/', views.add_question_choice, name="add_question_choice"),
    path('addquestionshort/', views.add_question_short, name="add_question_short"),

    path('updatequestion/<str:pk>/', views.update_question_long, name="update_question_long"),
    path('updatequestionshort/<str:pk>/', views.update_question_short, name="update_question_short"),
    path('updatequestionchoice/<str:pk>/', views.update_question_choice, name="update_question_choice"),


    path('deletequestion/<str:pk>/', views.delete_question_long, name="delete_question"),
    path('deleteshort/<str:pk>/', views.delete_question_short, name="delete_question_short"),
    path('deletechoice/<str:pk>/', views.delete_question_choice, name="delete_question_choice"),
  

]
