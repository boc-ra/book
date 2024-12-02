from django import forms
from .models import Bookdiary


class BookdiaryForm(forms.ModelForm):
    class Meta:
        model = Bookdiary
        fields = ('date', 'title', 'writer','text',)
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'book-title'}),
            'writer': forms.TextInput(attrs={'class': 'form-control', 'id': 'book-writer'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
