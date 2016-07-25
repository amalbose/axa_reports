from django.db import models

from testcases.models import TestCase

# Create your models here.
class Execution(models.Model):
    exec_id         = models.AutoField(primary_key=True)
    env             = models.CharField(max_length=500,blank=True, null=True)
    created_time    = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_time   = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return str(self.exec_id);
    
class ExecutionTC(models.Model):
    exec_tc_id       = models.AutoField(primary_key=True)
    tc_id            = models.ForeignKey(TestCase)
    exec_id          = models.ForeignKey(Execution)

    PASS = 'PASS'
    FAIL = 'FAIL'
    NORUN = 'NO RUN'
    SKIP = 'SKIP'
    STATUS_CHOICES = (
        (PASS, 'Pass'),
        (FAIL, 'Fail'),
        (NORUN, 'No Run'),
        (SKIP, 'Skip'),
    )
    status          = models.CharField(max_length=6, choices=STATUS_CHOICES, default=NORUN);
    executed_time    = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_time   = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return str(self.exec_tc_id);