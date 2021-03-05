from django import forms
from .models import Answer, HomeWork ,Video


class answerform(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('title','studentNumber','author', 'pdf')


class homeworkform(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = ('title', 'deadline','tozihat','pdf')


#class videoform(forms.ModelForm):
    class Meta:
        model = Video
        fields= ('title', 'video' )