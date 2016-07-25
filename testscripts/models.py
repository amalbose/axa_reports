from django.db import models

from testplans.models import TestPlan

# Create your models here.
class TestScript(models.Model):
    script_id       = models.AutoField(primary_key=True)
    plan_id         = models.ForeignKey(TestPlan)
    script_name     = models.CharField(max_length=200)
    owner           = models.CharField(max_length=200, blank=True, null=True)
    created_time    = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_time   = models.DateTimeField(auto_now_add=False, auto_now=True)
    active          = models.BooleanField(default='Yes')
    def __str__(self):
        return self.script_name;