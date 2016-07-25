from django.contrib import admin

# Register your models here.
from executions.models import Execution
from executions.models import ExecutionTC
from executions.models import ExecutionTS

admin.site.register(Execution)
admin.site.register(ExecutionTC)
admin.site.register(ExecutionTS)