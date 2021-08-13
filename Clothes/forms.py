from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from .models import Runs

class RunForm(ModelForm):
    class Meta:
        model = Runs
        fields = '__all__'
        # fields = ['target','mileage','duration','pace','shoe']
        # widget = {'duration':SelectDateWidget()}
# class CustomFormSet(ModelForm):
#      def __init__(self, *args, **kwargs):
#         super(RunForm, self).__init__(*args, **kwargs)
#         self.fields['duration'].widget = SelectDateWidget()