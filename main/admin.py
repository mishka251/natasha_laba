from django.contrib import admin
from .models import Patient, Measurement

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name')
    list_filter = ('name', )
    pass

@admin.register(Measurement)
class IDAdmin(admin.ModelAdmin):
    list_display = ("citation",)
    list_filter = ("datetime", )
    pass