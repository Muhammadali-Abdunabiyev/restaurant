from django import forms
from pages.models import *


class EmailForm(forms.ModelForm):

    class Meta:
        model = EmailModel
        fields = ['email']



class BookTableForms(forms.ModelForm):
    class Meta:
        model = BookTableModels
        fields = '__all__'
