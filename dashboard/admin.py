from django.contrib import admin
from .models import SubmitRequest, ServiceStatus, AssignTechnician

# Register your models here.

admin.site.register(SubmitRequest)
admin.site.register(ServiceStatus)
admin.site.register(AssignTechnician)