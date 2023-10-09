from django.db import models

GENDER_CHOICES =(
    ('gender','Male'),
    ('gender','Female'),
)

class registers(models.Model):
    firstname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES , max_length=128)
    
    
class admin_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    password = models.CharField(max_length=128)