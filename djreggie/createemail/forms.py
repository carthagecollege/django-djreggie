#Need these imports
from django import forms
from django.core import validators #Need this for custom validation
import datetime
from djreggie.createemail.models import EmailModel
import re

#The fields in this class represent the fields in the form
class EmailForm(forms.ModelForm):
    
    #Need to override __init__ to add custom validation, error messages, labels, etc
    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args,**kwargs)
        
        #Custom validation
        #self.fields['unique_id'].validators = [validators.RegexValidator(regex=('^\d{5,7}$'),message='Invalid carthage id',code='a')]
        #self.fields['requested_by'].validators = [validators.RegexValidator(regex=('^[a-zA-Z\']+[a-zA-Z\-\s\']+$'),message='Invalid name',code='a')]
        #self.fields['name_of_account_requested'].validators = [validators.RegexValidator(regex=('^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,4}$'), message='Invalid email', code='a')]
        #self.fields['purpose_of_account'].validators = [validators.RegexValidator(regex=('^.+$'), message='Enter the purpose of the account', code='a')]
        #self.fields['names_of_all_users'].validators = [validators.RegexValidator(regex=('^.+$'), message='Enter users', code='a')]
        
        #self.fields['name_of_account_requested'].label = "Email address you are requesting"
        
        #Custom error messages
        #self.fields['unique_id'].error_messages = {'required':'An id is required'}
        #self.fields['date'].error_messages = {'required':'A date is required'}
        #self.fields['requested_by'].error_messages = {'required':'A name is required'}
        #self.fields['name_of_account_requested'].error_messages = {'required':'An account email is required'}
        #self.fields['purpose_of_account'].error_messages = {'required':'A purpose is required'}
        #self.fields['names_of_all_users'].error_messages = {'required':'Users are required'}
        #self.fields['needed_until'].error_messages = {'required':'A date is required', 'invalid':'Date cannot be in the past'}
        
    def clean(self):
        cleaned_data = self.cleaned_data
        test = cleaned_data.get('needed_until')
        
        if test == None or test == "":
            msg = u"Invalid or past date"
            self._errors['needed_until'] = self.error_class([msg])
        else:  
            if test < datetime.date.today():
                msg2 = u"The date cannot be in the past!"
                self._errors["needed_until"] = self.error_class([msg2]) #Adds the error message to the field
                del cleaned_data["needed_until"]
        
        return cleaned_data
            
    #A function that will print values in a format, when we email the form
    def as_string(self):
        return '''
                Please check Django admin page for this new submission ->
        
                Unique ID: %s\n
                Requested by: %s\n
                Name of account: %s\n
                Purpose of account: %s\n
                Names of all users: %s\n
                Needed until: %s \n''' % (self.cleaned_data['unique_id'],
                                            #self.cleaned_data['date'],
                                            self.cleaned_data['requested_by'],
                                            self.cleaned_data['name_of_account_requested'],
                                            self.cleaned_data['purpose_of_account'],
                                            self.cleaned_data['names_of_all_users'],
                                            self.cleaned_data['needed_until'])    
    
    def clean_unique_id(self):
        data = self.cleaned_data['unique_id']
        if not re.match(r'^\d{5,7}$', data):
            raise forms.ValidationError('Invalid carthage id')
        return data
    
    def clean_requested_by(self):
        data = self.cleaned_data['requested_by']
        if not re.match(r'^[a-zA-Z\']+[a-zA-Z\-\s\']+$', data):
            raise forms.ValidationError('Invalid name')
        return data
    
    
    #Global options    
    class Meta:
        model = EmailModel #All of the fields come from our model, 'EmailModel'
        widgets = { #Changes the display of fields
            #'date' : forms.DateInput(attrs={'type':'date'}), Keep this commented out unless you want to add 'date' back in
            'needed_until' : forms.DateInput(attrs={'type':'date'}), #Datepicker 
            'purpose_of_account': forms.Textarea(attrs={'cols': 25, 'rows': 5}), #Textarea
            'names_of_all_users': forms.Textarea(attrs={'cols': 25, 'rows': 5}),
        }    
    
    
