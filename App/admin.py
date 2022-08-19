from django.contrib import admin
from .models import Patient

admin.site.site_header = 'Hospital'
# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'age', 'gender', 'created_on']
    search_fields = ['id', 'name', 'phone', 'email']
    list_filter = ['gender', 'age']
    list_per_page = 10


admin.site.register(Patient, PatientAdmin)

    

