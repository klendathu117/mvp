from django.shortcuts import render, redirect, get_object_or_404
from .models import AlertTemplate, ThirdPartyAlert
from .forms import AlertTemplateForm, ThirdPartyAlertForm
from django.urls import reverse

def create_template(request):
    if request.method == 'POST':
        form = AlertTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_templates')
    else:
        form = AlertTemplateForm()
    return render(request, 'alerts/create_template.html', {'form': form})

def list_templates(request):
    templates = AlertTemplate.objects.all()
    return render(request, 'alerts/list_templates.html', {'templates': templates})

def map_alert(request):
    sidebar_links = [
        {'name': 'Map Alerts', 'url': reverse('map_alert')},
        {'name': 'Home', 'url': reverse('home')},
        {'name': 'Create Template', 'url': reverse('create_template')},
        {'name': 'My Templates', 'url': reverse('list_templates')},
        {'name': 'Mappings', 'url': reverse('view_mappings')},
    ]
    '''
    if request.method == 'POST':
        form = ThirdPartyAlertForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'alerts/map_alert.html', {'form': form}, {'sidebar_links': sidebar_links})
    else:
        form = ThirdPartyAlertForm()
    '''
    return render(request, 'alerts/map_alert.html', {'sidebar_links': sidebar_links})

def view_mappings(request):
    mappings = ThirdPartyAlert.objects.select_related('template').all()
    return render(request, 'alerts/view_mappings.html', {'mappings': mappings})

def home(request):
    return render(request, 'alerts/home.html')

def view_a_OLD(request):
    return render(request, 'alerts/view_a.html')
