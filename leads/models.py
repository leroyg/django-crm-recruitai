from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
from xmlrpc.client import FastMarshaller
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
    
    
class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_email = models.CharField(max_length=50, blank=False)
    contact_phone = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.user.email


class Lead(models.Model):
    CONTACT_PREFERNCES_CHOICES = [
        ('Txt', 'Text Message'),
        ('Email', 'Email Message'),
        ('Phone', 'Phone Call'),
    ]
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    contact_email = models.CharField(max_length=50, blank=False)
    contact_phone = models.CharField(max_length=20, blank=False)
    
    class_year = models.CharField(max_length=6, help_text='Please enter the semester (FA for Fall, and SP for Spring) and year of your first semester, for example FA23.')
    high_school = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=25)
    contact_preference = models.CharField(max_length=30,choices=CONTACT_PREFERNCES_CHOICES)
    
    guardian_contact_name = models.CharField(max_length=120)
    guardian_contact_phone = models.CharField(max_length=20)
    guardian_contact_email = models.CharField(max_length=100, default="None")
    
    application_status = models.BooleanField(default=False)
    transcript_status = models.BooleanField(default=False)
    fafsa_status = models.BooleanField(default=False)
    
    last_contact_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True)
    
    athlete_files = models.FileField(blank=True, null=True)
    recruiter = models.ForeignKey("Recruiter", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"  




    
    