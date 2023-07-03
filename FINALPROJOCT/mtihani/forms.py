from django import forms
from .models import Exam,Mtihani, MtihaniTaarifa

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'



class MtihaniForm(forms.ModelForm):
    # examdate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Mtihani
        fields = '__all__'        

class MtihaniTaarifaForm(forms.ModelForm):
    class Meta:
        model = MtihaniTaarifa
        fields = '__all__'        