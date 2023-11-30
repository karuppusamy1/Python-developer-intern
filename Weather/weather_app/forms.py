# weather_app/forms.py

from django import forms
from .models import WeatherAlert

class WeatherAlertForm(forms.ModelForm):
    class Meta:
        model = WeatherAlert
        fields = ['city', 'email']

class WeatherForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)
    latitude = forms.CharField(widget=forms.HiddenInput(), required=False)
    longitude = forms.CharField(widget=forms.HiddenInput(), required=False)