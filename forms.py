from django import forms
from .models import DeptModel,StuModel

class DeptForm(forms.ModelForm):
    class Meta:
        model=DeptModel
        fields="__all__"

class StuForm(forms.ModelForm):
    class Meta:
        model=StuModel
        fields="__all__"

