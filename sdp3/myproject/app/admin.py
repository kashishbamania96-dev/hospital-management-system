from django.contrib import admin
from .models import Patient, Doctor, Appointment


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	list_display = ('name', 'medical_record_number', 'age', 'contact')
	search_fields = ('name', 'medical_record_number')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
	list_display = ('name', 'specialty', 'contact')
	search_fields = ('name', 'specialty')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('patient', 'doctor', 'scheduled_at', 'status')
	list_filter = ('status', 'scheduled_at')
	search_fields = ('patient__name', 'doctor__name')