from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', include('django.contrib.auth.urls')),
    
    path('add_patient/', views.add_patient, name='add_patient'),
    path('patient/<str:patient_id>', views.patient, name='patient'),
    path('edit_patient/', views.edit_patient, name='edit_patient'),
    path('delete_patient/<str:patient_id>', views.delete_patient, name='delete_patient'),
    path('backend/', views.backend, name='backend'),
]
