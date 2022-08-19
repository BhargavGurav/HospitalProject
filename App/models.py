from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Patient(models.Model):

    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
        ('T', 'T')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField()
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=7, choices=GENDER)
    created_on = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
