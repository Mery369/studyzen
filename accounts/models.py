from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add a field to distinguish the user role (Student, Therapist, Instructor)
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('therapist', 'Therapist'),
        ('instructor', 'Instructor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Fields for therapist/instructor profiles
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    speciality = models.CharField(max_length=200, blank=True, null=True)
    availability = models.TextField(blank=True, null=True)  # Availability slots description
    
    # Flag to indicate whether this profile is a therapist or instructor
    is_therapist = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Profile"