from django.db import models

# Hospital management models
class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    contact = models.CharField(max_length=50, blank=True)
    medical_record_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} ({self.medical_record_number})"


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Dr. {self.name} — {self.specialty}"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='appointments')
    scheduled_at = models.DateTimeField()
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"{self.patient} - {self.doctor} @ {self.scheduled_at.strftime('%Y-%m-%d %H:%M')}"