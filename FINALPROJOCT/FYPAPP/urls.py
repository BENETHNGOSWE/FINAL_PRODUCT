from django.urls import path
from . import views
from FYPAPP import views

app_name = 'FYPAPP'

urlpatterns = [
    path('', views.home.as_view(), name='homepage'),
    path('addcourse/', views.add_course, name='add_course'),
    path('addmodule', views.add_module, name='add_module'),
    path('dashboard/', views.dashboard.as_view(), name='dashboard'),
    # path('addquestion/', views.add_question, name='add_question'),
    # path('addquestion/', views.add_question, name="data_create"),
    # path('data/', views.question_manage, name="benny"),



    
    path('addmaswali/', views.add_maswali, name="da"),
    path('data/', views.question_manage, name="question_manage"),
]
