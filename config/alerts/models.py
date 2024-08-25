from django.db import models

class AlertTemplate(models.Model):
    name = models.CharField(max_length=255)
    template = models.JSONField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ThirdPartyAlert(models.Model):
    name = models.CharField(max_length=255)
    alert_data = models.JSONField()
    template = models.ForeignKey(AlertTemplate, related_name='third_party_alerts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} mapped to {self.template.name}"