
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Street(models.Model):
    street_name = models.CharField(max_length=255)
    num_grown_up_females = models.IntegerField()
    num_grown_up_males = models.IntegerField()
    num_children = models.IntegerField()
    total_population = models.IntegerField()
    km_square = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.street_name

class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    nida_id = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class HealthFacility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    nida_id = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.ForeignKey(Street, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    date_reported = models.DateField(auto_now_add=True)
    time_reported = models.TimeField(auto_now_add=True, null=True, blank=True)
    health_facility = models.ForeignKey(HealthFacility, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Deceased(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    date_of_death = models.DateField(auto_now_add=True)
    time_of_death = models.TimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.last_name}'

class Recovered(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    date_of_recovery = models.DateField(auto_now_add=True)
    time_of_recovery = models.TimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.last_name}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        NormalUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not instance.is_superuser:
        instance.normaluser.save()
