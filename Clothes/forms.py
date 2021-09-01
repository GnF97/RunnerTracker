from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from .models import Runs, Shoes, Clothets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class RunFormM(forms.ModelForm):
    shoe_name = forms.CharField(required=True)

    class Meta:
        model = Runs
        exclude = ('shoe',)

    def __init__(self, *args, **kwargs):
        super(RunFormM, self).__init__(*args, **kwargs)
        if self.instance and not self.data:
            self.initial['shoe_name'] = self.instance.shoe.nameS

    def save(self, commit=True):
        shoe_name =  self.cleaned_data['shoe_name']
        nameS, _ = Shoes.objects.get_or_create(nameS=shoe_name)
        instance = super(RunFormM, self).save(commit=False)
        instance.shoe = nameS
        if commit:
            instance.save()
        return instance
        # instance = self.save(commit=False)
        # instance.nameS = nameS
        # if commit == True:
        #     instance.save()
        # return instance
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class ClothsetForm(ModelForm):
    class Meta:
        model = Clothets
        fields = '__all__'
        exclude = ['user']
