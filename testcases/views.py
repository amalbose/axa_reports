from django.shortcuts import render

from django.http import HttpResponse
from .models import TestCase

# Create your views here.
def index(request):
    latest_testcase_list = TestCase.objects.order_by('-created_time')[:5]
    context = {'title':'Test Cases','latest_testcase_list': latest_testcase_list}
    return render(request, "testcases/index.html", context)


def detail(request, script_id):
    return HttpResponse("You are seeing testcase %s " % script_id)