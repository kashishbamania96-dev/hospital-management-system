from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'appointments', views.AppointmentViewSet)

urlpatterns = [
    # Web URLs
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('view-patients/', views.view_patients, name='view_patients'),
    path('delete-patient/<int:id>/', views.delete_patient, name='delete_patient'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('view-doctors/', views.view_doctors, name='view_doctors'),
    path('delete-doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),
    path('add-appointment/', views.add_appointment, name='add_appointment'),
    path('view-appointments/', views.view_appointments, name='view_appointments'),
    path('delete-appointment/<int:id>/', views.delete_appointment, name='delete_appointment'),
    
    # REST API URLs
    path('api/', include(router.urls)),
    path('api/patients/', views.api_patient_list, name='api_patient_list'),
    path('api/patients/create/', views.api_patient_create, name='api_patient_create'),
    path('api/patients/<int:pk>/', views.api_patient_detail, name='api_patient_detail'),
    path('api-auth/', include('rest_framework.urls')),
]