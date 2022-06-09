from django.contrib import admin
from .models import Sensor, Measurment
from django.forms import BaseInlineFormSet

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['name']

@admin.register(Measurment)
class MeasurmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature', 'created_at', 'sensors']
    list_filter = ['sensors', 'id']
