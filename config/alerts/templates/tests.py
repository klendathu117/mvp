from django.test import TestCase
from django.db.models import AlertTemplate, ThirdPartyAlert

class AlertTemplateTestCase(TestCase):
    def setUp(self):
        AlertTemplate.objects.create(name="Test Template", template={"key": "value"})

    def test_template_creation(self):
        template = AlertTemplate.objects.get(name="Test Template")
        self.assertEqual(template.template, {"key": "value"})

class ThirdPartyAlertTestCase(TestCase):
    def setUp(self):
        template = AlertTemplate.objects.create(name="Test Template", template={"key": "value"})
        ThirdPartyAlert.objects.create(name="Test Alert", alert_data={"alert_key": "alert_value"}, template=template)

    def test_alert_mapping(self):
        alert = ThirdPartyAlert.objects.get(name="Test Alert")
        self.assertEqual(alert.alert_data, {"alert_key": "alert_value"})
        self.assertEqual(alert.template.name, "Test Template")
