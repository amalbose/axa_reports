from django.shortcuts import render

from django.http import HttpResponse
from testscripts.models import TestScript

# Create your views here.
def index(request):
    latest_testscript_list = TestScript.objects.order_by('-created_time')[:5]
    context = {'title':'Test Scripts','latest_testscript_list': latest_testscript_list}
    return render(request, "testscripts/index.html", context)


def detail(request, script_id):
    return HttpResponse("You are seeing testscript %s " % script_id)