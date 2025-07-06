from django.urls import path
from django.contrib import admin
from .views import CreateSensor, home_view, ModifySensor, AddMeasurement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('sensors/', CreateSensor.as_view()),
    path('sensors/<int:pk>/', ModifySensor.as_view()),
    path('measurements/', AddMeasurement.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
