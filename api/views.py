from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from executions.models import ExecutionTC
from rest_framework import viewsets

from .serializers import ExecutionTCSerializer
from django.contrib.auth.models import User
from testplans.models import TestPlan

# Create your views here.
def index(request):
    response = JsonResponse({})
    return response


class ExecutionTCViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExecutionTC.objects.all().order_by('-executed_time')
    serializer_class = ExecutionTCSerializer