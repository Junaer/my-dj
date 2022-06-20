# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Sensor, Measurment
from .serializers import SensorSerializer, MeasurmentSerializer, SensorsSerializer, MainMeasurmentSerializer
from rest_framework.generics import RetrieveAPIView

class APISensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        name = request.data['name']
        description = request.data['description']
        Sensor(name=name, description=description).save()
        return Response(f'{name}: {description} created')


class APISensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        description = request.data['description']
        Sensor.objects.filter(id=int(pk)).update(description=description)
        return Response(f'{description} update')

class APIMeasurments(ListAPIView):
    queryset = Measurment.objects.all()
    serializer_class = MainMeasurmentSerializer

    def post(self, request):
        temperature = float(request.data['temperature'])
        sensors = int(request.data['sensors'])
        Measurment(temperature=temperature, sensors_id=sensors).save()
        return Response(f'{temperature}: sensor number - {sensors} created')

class APIMeasurment(RetrieveAPIView):
    queryset = Measurment.objects.all()
    serializer_class = MeasurmentSerializer

    def patch(self, request, pk):
        temperature = request.data['temperature']
        Measurment.objects.filter(id=int(pk)).update(temperature=temperature)
        return Response(f'{temperature} update')
