from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Type your question...'}),
            'author': forms.TextInput(attrs={'placeholder': 'Name or leave blank for Anonymous'}),
        }

