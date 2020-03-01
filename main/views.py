from django.shortcuts import render
from main.models import Patient, Measurement
# Create your views here.

def index(request):
    patinets = Patient.objects.all()
    measurement = Measurement.objects.all()
    return render(request, 'index.html', {'patients':patinets, 'measurement':measurement})