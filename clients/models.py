from django.db import models

class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    CONTACT_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('none', 'None'),
    ]
    EDUCATION_CHOICES=[
        ('slc','SLC'),
        ('+2','+2'),
        ('Bachelor','Bachelor'),
    ]

    name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='client_profile_images')

    gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    education_background = models.CharField(max_length=50,choices=EDUCATION_CHOICES)
    preferred_contact = models.CharField(max_length=10, choices=CONTACT_CHOICES)

    # Additional fields or relationships can be added here

    def __str__(self):
        return self.name

