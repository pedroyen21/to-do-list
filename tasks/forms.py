from django import forms
from requests import request
from .models import Task
from django.utils.timezone import now


class UpdateForm(forms.ModelForm):
   conc_date = forms.DateField(
      label='Conclusion Date',
      widget= forms.DateInput(
         format= '%Y-%m-%d',
         attrs={
            'type': 'date',
            
         },
      ), input_formats=['%Y-%m-%d']   
   )
   class Meta: 
      model  = Task
      fields = ('name', 'description', 'conc_date')
   
