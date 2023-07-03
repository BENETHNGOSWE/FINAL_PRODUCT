from django.db import models
from django.contrib.auth.models import User
# Create your models here.

questionsection = (
    ("YES", "YES"),
    ("NO", " NO"),
    
)
questiontype = (
    ("multichoice Questions", "multichoice Questions"),
    ("short answers Questions", "short answers Questions"),
    ("long answers Questions", "long answers Questions"),
)

questionlevel = (
    ("Normal", "Normal"),
    ("Medium", "Medium"),
    ("Hard", "Hard")
)


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    courseName = models.CharField(max_length=30)
    courseCode = models.CharField(max_length=30)

    def __str__(self):
        return self.courseName

class Masomo(models.Model):
    moduleName = models.CharField(max_length=30)
    moduleCode = models.CharField(max_length=30)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.moduleName

class Topic(models.Model):
    topicNumber = models.IntegerField()
    topicName = models.CharField(max_length=30)
    module = models.ForeignKey(Masomo, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.topicName

class QuestionType(models.Model):
    questiontype = models.CharField(max_length=30)

    def __str__(self):
        return self.questiontype


class QuestionSection(models.Model):
    questionsection = models.CharField(choices=questionsection, null=True, max_length=10)

    def __str__(self):
        return self.questionsection

class Department(models.Model):
    deptname = models.CharField(max_length=100, null=True, blank=True)
  
    def __str__(self):
        return self.deptname

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
# class Question(models.Model):
#     questionType = models.ForeignKey(QCategory, on_delete=models.CASCADE, default='multichoice_Questions')
#     questionLevel = models. CharField(max_length=30, null=True, choices=questionlevel)
#     somo = models.ForeignKey('Masomo', on_delete=models.CASCADE)
#     topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
#     questionText = models.TextField ()
    

#     def __str__(self): 
#         return self.questionText

class QuestionChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    somo = models.ForeignKey('Masomo', on_delete=models.CASCADE, null=True, blank=True)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, null=True, blank=True)
    option1 = models.CharField(max_length=100, null=True, blank=True)
    option2 = models.CharField(max_length=100, null=True, blank=True)
    option3 = models.CharField(max_length=100, null=True, blank=True)
    option4 = models.CharField(max_length=100, null=True, blank=True)
    answer = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.question

class QuestionShortterm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    somo = models.ForeignKey('Masomo', on_delete=models.CASCADE, null=True, blank=True)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(max_length=100, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)


class QuestionLongTerm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    somo = models.ForeignKey('Masomo', on_delete=models.CASCADE,null=True, blank=True)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField (max_length=100, null=True, blank=True)
    answer = models.TextField (null=True, blank=True)















