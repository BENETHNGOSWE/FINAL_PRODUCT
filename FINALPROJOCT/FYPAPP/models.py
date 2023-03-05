from django.db import models

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
    courseName = models.CharField(max_length=30)
    courseCode = models.CharField(max_length=30)

    def __str__(self):
        return self.courseName

class Masomo(models.Model):
    moduleName = models.CharField(max_length=30)
    moduleCode = models.CharField(max_length=30)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
    moduleTeacher = models.CharField(max_length=30)

    def __str__(self):
        return self.moduleName

class Topic(models.Model):
    topicNumber = models.IntegerField()
    topicName = models.CharField(max_length=30)
    module = models.ForeignKey('Masomo', on_delete=models.CASCADE)
    def __str__(self):
        return self.topicName

# class QuestionType(models.Model):
#     questiontype = models.CharField(max_length=30)

#     def __str__(self):
#         return self.questiontype


class QuestionSection(models.Model):
    questionsection = models.CharField(choices=questionsection, null=True, max_length=10)

    def __str__(self):
        return self.questionsection

# class QuestionLevel(models.Model):
#     questionLevel = models.CharField(max_length=30)

#     def __str__(self):
#         return self.questionLevel


class Question(models.Model):
    questiontype = models.CharField(max_length=30, null=True, choices=questiontype)
    questionLevel = models. CharField(max_length=30, null=True, choices=questionlevel)
    somo = models.ForeignKey('Masomo', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    questionText = models.TextField ()
    

    def __str__(self): 
        return self.questionText
















#         <div class="container card p-3 mt-5 border-dark" style="width: 95%;">
# 	<table>
# 		<thead>
# 			<tr>
# 				<th>Maswali</th>
# 				<th>Ainayaswali</th>
# 			</tr>
# 		</thead>

# 		{% for data in question %}
# 		<tr>
# 			<td>{{data.Maswali}}</td>
# 			<td>{{data.Ainayaswali}}</td>
# 		</tr>
# 		{% endfor %}
# 	</table>

# </div>