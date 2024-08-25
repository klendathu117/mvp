from django import forms
from .models import AlertTemplate, ThirdPartyAlert

class AlertTemplateForm(forms.ModelForm):
    class Meta:
        model = AlertTemplate
        fields = ['name', 'template', 'description']

class ThirdPartyAlertForm(forms.ModelForm):
    class Meta:
        model = ThirdPartyAlert
        fields = ['name', 'alert_data', 'template']
