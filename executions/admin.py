from django.contrib import admin

# Register your models here.
from .models import Execution
from .models import ExecutionTC

admin.site.register(Execution)
admin.site.register(ExecutionTC)