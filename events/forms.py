from django import forms
from .models  import Events
from django.contrib.admin.widgets import AdminDateWidget


class EventsForm (forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Events
        fields = ['name','location','date1']


