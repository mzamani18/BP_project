from django import forms
from .models import Answer


class answerform(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('title', 'author', 'pdf')
