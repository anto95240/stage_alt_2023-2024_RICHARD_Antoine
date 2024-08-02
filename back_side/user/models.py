from django.db import models
from django.contrib.auth.hashers import make_password

class UserLevel(models.Model):
    Class = models.CharField(max_length=255)

    def __str__(self):
        return self.Class

class UserSpecialization(models.Model):
    Specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.Specialization

class User(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Address = models.CharField(max_length=255)
    Email = models.EmailField(max_length=100, unique=True)
    Age = models.CharField(max_length=255, null=True, blank=True)
    Password = models.CharField(max_length=255)
    Specialization = models.ForeignKey(UserSpecialization, on_delete=models.CASCADE, related_name='spe_user', null=True, blank=True)
    Photo = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher')
    )
    Class = models.ForeignKey(UserLevel, on_delete=models.CASCADE, related_name='class_user', null=True, blank=True)
    Role = models.CharField(max_length=20, choices=ROLE_CHOICES) 

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"{self.Class.Class if self.Class else None } - {self.Specialization.Specialization if self.Specialization else 'Aucune spécialité'} -- {self.FirstName} {self.LastName} ({self.Role})"

