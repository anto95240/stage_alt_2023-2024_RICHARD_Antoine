from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Address = models.CharField(max_length=255)
    Email = models.EmailField(max_length=100, unique=True)
    Age = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=255)
    Photo = models.BinaryField(null=True, blank=True)
    Specialization = models.CharField(max_length=100, null=True, blank=True)
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    Role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        managed = False  
        db_table = 'user_table'  
        ordering = ('-UserId',)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
    
    def save(self, *args, **kwargs):
        if self.Password:
            self.Password = make_password(self.Password)
        super().save(*args, **kwargs)
