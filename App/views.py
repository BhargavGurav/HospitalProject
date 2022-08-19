from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Patient
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_control  # when we logout and again press back we still logged in so to remove that 

# Create your views here.
def home(request):
    return render(request, 'home.html')


@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q) | Q(age__icontains=q) | Q(gender__icontains=q) 
        ).order_by('id')

    else:
        all_patient_list = Patient.objects.all().order_by('id')
    paginator = Paginator(all_patient_list, 8)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)

    return render(request, 'backend.html' , {'patients' : all_patient})
    

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url="login")
def add_patient(request):
    if request.method=='POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']

        if request.POST['note']:
            note = request.POST['note']
            data = Patient(name=name, phone=phone, email=email, age=age, gender=gender, note=note)

        else:
            data = Patient(name=name, phone=phone, email=email, age=age, gender=gender)
        data.save()
        messages.success(request, 'Patient added successfully')
        return HttpResponseRedirect('/backend')

    else:
        return render(request, 'add.html')


@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url="login")
def edit_patient(request):
    if request.method=='POST':
        patient = Patient.objects.get(name=request.POST['name'])
        patient.phone = request.POST['phone']
        patient.email = request.POST['email']
        patient.age = request.POST['age']
        patient.gender = request.POST['gender']
        if request.POST['note']:
            patient.note = request.POST['note']
            patient.save()
        else:
            patient.save()

        messages.success(request, 'Patient updated successfully')
        return HttpResponseRedirect('/backend')

    return render(request, 'edit.html')


@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url="login")
def patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if patient != None:
        return render(request, 'edit.html', {'patient' : patient})

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url="login")
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    
    messages.success(request, 'Patient deleted successfully')
    return HttpResponseRedirect('/backend')
    


    