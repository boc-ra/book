from django import forms
from .models import Bookdiary

# 読書記録用フォーム
class DateInput(forms.DateInput):
    input_type = 'date'
class BookdiaryForm(forms.ModelForm):
    class Meta:
        model = Bookdiary
        fields = ('date', 'title', 'writer','text',)
        widgets = {
            'date': DateInput(attrs={'class': 'form-control', 'id': 'book-date'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'book-title'}),
            'writer': forms.TextInput(attrs={'class': 'form-control', 'id': 'book-writer'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

# 読書記録検索フォーム

