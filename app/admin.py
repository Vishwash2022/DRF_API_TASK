from django.contrib import admin
from .models import Machine, Patient, Dose


admin.site.register(Machine)
admin.site.register(Patient)
admin.site.register(Dose)