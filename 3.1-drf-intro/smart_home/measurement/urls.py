from django.urls import path
from . import views
from .views import APISensors, APISensor, APIMeasurment, APIMeasurments

urlpatterns = [
    path('sensors/', APISensors.as_view(), name='sensors'),
    path('sensors/<pk>/', APISensor.as_view(), name='sensor'),
    path('measurments', APIMeasurments.as_view(), name='measurments'),
    path('measurment/<pk>/', APIMeasurment.as_view(), name='measurment')
]
