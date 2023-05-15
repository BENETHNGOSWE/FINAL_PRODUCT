from django import forms
from .models import Category,Masomo, Course, QuestionChoice, QuestionShortterm, QuestionLongTerm, Department


class MasomoForm(forms.ModelForm):
    class Meta:
        model = Masomo
        fields = '__all__'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionLongTerm
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'      

class QuestionChoiceForm(forms.ModelForm):
    class Meta:
        model = QuestionChoice
        fields = '__all__'
 
class QuestionShorttermForm(forms.ModelForm):
    class Meta:
        model = QuestionShortterm   
        fields = '__all__'   

        
class QuestionCountForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
           
# class QuestionForm(models.Model):
#     questiontype = models.ForeignKey('QuestionType', on_delete=models.CASCADE)
#     questionLevel = models. ForeignKey('QuestionLevel', on_delete=models.CASCADE)
#     somo = models.ForeignKey('Masomo', on_delete=models.CASCADE)
#     topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
#     questionText = models.TextField ()
    