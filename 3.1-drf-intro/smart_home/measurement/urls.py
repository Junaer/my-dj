from django.urls import path
from . import views
from .views import MyAPI, MyAPIsensor

urlpatterns = [
    path('sensors/', MyAPI.as_view(), name='myapi'),
    path('sensors/<pk>/', MyAPIsensor.as_view())
]
