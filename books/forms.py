from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Book

class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='您確認要刪除嗎？')