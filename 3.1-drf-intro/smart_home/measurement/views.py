# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


def home_view(request):
    return HttpResponse("Стартовая страница")

class CreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class ModifySensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'pk'

class AddMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Status': 'Recorded'})
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
