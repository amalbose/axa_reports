from django.shortcuts import render
from executions.models import ExecutionTC, Execution

# Create your views here.


def index(request):
    latest_exec_list = Execution.objects.order_by('-created_time')[:5]
    context = {'title':'Executions', 'latest_exec_list': latest_exec_list}
    return render(request, "executions/index.html", context)

def detail(request, exec_id):
    exec_tc_list = ExecutionTC.objects.select_related('tc_id__script_id__script_name').all().filter(exec_id=exec_id)
    context = {'title':'Execution Status', 'exec_tc_list': exec_tc_list}
    return render(request, "executions/detail.html", context)
