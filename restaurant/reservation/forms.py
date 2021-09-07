from django import forms
from .models import Reservation

# class ReserveForm(forms.Form):
#     subject = forms.CharField()
#     from_email = forms.EmailField(required=True)
#     # message = forms.CharField(widget=forms.Textarea,required=True)

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        subject = forms.CharField()
        email = forms.EmailField(required=True)
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }