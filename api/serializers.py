'''
Created on Jul 24, 2016

@author: amalbose
'''
from executions.models import ExecutionTC
from rest_framework import serializers
from django.contrib.auth.models import User
from testplans.models import TestPlan


class ExecutionTCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionTC
        fields = ('exec_tc_id', 'tc_id', 'status', 'executed_time')
