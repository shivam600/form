from django import forms
from .models import Destination
class DestinationForm(forms.ModelForm):

    class Meta:
        model=Destination
        fields=("name","employee_code","phone_no","position")
        labels={
            "name": "FULLNAME",
            "employee_code":"EMP CODE",
            "position":"POSITION"
        }

    def __init__(self,*args,**kwargs):
        super(DestinationForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="select"
        self.fields['employee_code'].required=False


        

