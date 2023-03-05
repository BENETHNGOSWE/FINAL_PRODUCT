from django.contrib import admin
from .models import Course, Masomo, Question, Topic, QuestionSection

# Register your models here.
admin.site.register(Course)
admin.site.register(Masomo)
admin.site.register(Question)
admin.site.register(Topic)
admin.site.register(QuestionSection)
# admin.site.register(QuestionType)
# admin.site.register(QuestionLevel)