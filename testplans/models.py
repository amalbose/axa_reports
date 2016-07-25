from django.db import models

# Create your models here.
class TestPlan(models.Model):
    plan_id         = models.AutoField(primary_key=True)
    testplan_id     = models.CharField(max_length=50,blank=True, null=True)
    testplan_name   = models.CharField(max_length=200)
    owner           = models.CharField(max_length=200, blank=True, null=True)
    created_time    = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_time   = models.DateTimeField(auto_now_add=False, auto_now=True)
    active          = models.BooleanField(default='Yes')
    def __str__(self):
        return self.testplan_name;
    