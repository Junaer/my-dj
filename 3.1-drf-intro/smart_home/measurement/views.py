# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Sensor, Measurment
from .serializers import SensorSerializer, MeasurmentSerializer, SensorsSerializer
from rest_framework.generics import RetrieveAPIView

# @api_view(['GET'])
# def my_api(request):
#     sensors = Sensor.objects.all()
#     ser = SensorSerializer(sensors, many=True)
#     data = {'sensors'}
#     return Response(ser.data)

# class MyAPI(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         ser = SensorSerializer(sensors, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         return Response({'status': 'ok'})

class MyAPI(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        name = request.data['name']
        description = request.data['description']
        Sensor(name=name, description=description).save()
        return Response(SensorsSerializer)

class MyAPIsensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
