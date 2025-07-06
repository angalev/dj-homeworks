from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Sensor, Measurement


@admin.register(Sensor)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Measurement)
class TeacherAdmin(admin.ModelAdmin):
    pass