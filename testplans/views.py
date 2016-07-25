from django.shortcuts import render

from django.http import HttpResponse
from .models import TestPlan

# Create your views here.
def index(request):
    latest_testplan_list = TestPlan.objects.order_by('-created_time')[:5]
    context = {'title':'Test Plans','latest_testplan_list': latest_testplan_list}
    return render(request, "testplans/index.html", context)

def detail(request, plan_id):
    return HttpResponse("You are seeing testplan %s " % plan_id)

def showScripts(request, plan_id):
    return HttpResponse("You are seeing scripts for testplan %s " % plan_id)
