from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'

    def __str__(self):
        return self.name

class Measurment(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    sensors = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurments'
    )

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
