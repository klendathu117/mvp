from django.contrib import admin
from .models import AlertTemplate, ThirdPartyAlert

admin.site.register(AlertTemplate)
admin.site.register(ThirdPartyAlert)

