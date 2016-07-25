from django.db import models

from testscripts.models import TestScript

# Create your models here.
class TestCase(models.Model):
    tc_id           = models.AutoField(primary_key=True)
    script_id       = models.ForeignKey(TestScript)
    tc_name         = models.CharField(max_length=200)
    owner           = models.CharField(max_length=200, blank=True, null=True)
    created_time    = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_time   = models.DateTimeField(auto_now_add=False, auto_now=True)
    active          = models.BooleanField(default='Yes')
    def __str__(self):
        return self.tc_name;