from rest_framework import serializers
from .models import Sensor, Measurment

class MainMeasurmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurment
        fields = ['id', 'temperature', 'created_at', 'sensors']

class MeasurmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurment
        fields = ['temperature', 'created_at']

class SensorSerializer(serializers.ModelSerializer):
    measurments = MeasurmentSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurments']

class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

