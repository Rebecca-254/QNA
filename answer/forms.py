from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['responder', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your answer...'}),
            'responder': forms.TextInput(attrs={'placeholder': 'Name or leave blank for Anonymous'}),
        }

