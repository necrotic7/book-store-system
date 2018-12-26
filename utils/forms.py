from django import forms





class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='您確認要刪除嗎？')