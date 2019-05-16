from django import forms

class LocationForm(forms.Form):
    location = forms.CharField(label='Your Surburb?', max_length=100)