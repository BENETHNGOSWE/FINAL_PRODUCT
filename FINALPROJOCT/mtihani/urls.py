from django.urls import path
from . import views


app_name = 'mtihani'

urlpatterns = [
    path('addexam/', views.add_exam, name="add_exam"),
    path('exam/', views.exam_manage, name="exam_manage")
]