from django.contrib import admin
from .models import Patient, Number

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass

@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    pass