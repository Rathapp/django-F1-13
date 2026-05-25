from django.contrib import admin
from .models import Patient,doctor,appointment

# Register your models here.
admin.site.register(Patient)
admin.site.register(doctor)
admin.site.register(appointment)