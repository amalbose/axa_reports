from django.db import models

from testcases.models import TestCase
from testscripts.models import TestScript
from django.template.defaultfilters import default

# Create your models here.

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
    
    
class Execution(models.Model):
    exec_id         = models.AutoField(primary_key=True)
    env             = models.CharField(max_length=500,blank=True, null=True)
    created_time    = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_time   = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return str(self.exec_id);
    
class ExecutionTS(models.Model):
    exec_ts_id       = models.AutoField(primary_key=True)
    script_id        = models.ForeignKey(TestScript)
    exec_id          = models.ForeignKey(Execution)
    passCount        = models.IntegerField(default=0)
    failCount        = models.IntegerField(default=0)
    noRunCount       = models.IntegerField(default=0)
    totalCount       = models.IntegerField(default=0)
    executed_time    = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_time    = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return str(self.exec_ts_id);

class ExecutionTC(models.Model):
    exec_tc_id       = models.AutoField(primary_key=True)
    tc_id            = models.ForeignKey(TestCase)
    exec_ts_id       = models.ForeignKey(ExecutionTS)
    status           = models.CharField(max_length=6, choices=STATUS_CHOICES, default=NORUN);
    executed_time    = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_time    = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return str(self.exec_tc_id);
    
