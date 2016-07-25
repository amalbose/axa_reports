from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from dashboard import common


def index(request):
    context = {
    "title" : common.APPLICATION_NAME
    }
    return render(request,"dashboard/home.html" , context);