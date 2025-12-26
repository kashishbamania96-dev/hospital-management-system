from rest_framework import serializers
from .models import Patient, Doctor, Appointment


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'gender', 'contact', 'medical_record_number']
        read_only_fields = ['id']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact']
        read_only_fields = ['id']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'scheduled_at', 'reason', 'status']
        read_only_fields = ['id']
