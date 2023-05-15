from django.contrib import admin
from .models import Category,Course,QuestionChoice, Masomo, Topic, QuestionSection, Department, QuestionShortterm, QuestionLongTerm

# Register your models here.
admin.site.register(Course)
admin.site.register(Masomo)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(QuestionSection)
admin.site.register(Department)
admin.site.register(QuestionChoice)
admin.site.register(QuestionShortterm)
admin.site.register(QuestionLongTerm)