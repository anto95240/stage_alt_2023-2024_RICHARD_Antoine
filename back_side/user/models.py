from django.db import models
from doc.models import Document
from django.contrib.auth.hashers import make_password

class UserLevel(models.Model):
    classe = models.CharField(max_length=255)

    def __str__(self):
        return self.classe

class UserSpecialization(models.Model):
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.specialization

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    age = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)
    specialization = models.ForeignKey(UserSpecialization, on_delete=models.CASCADE, related_name='spe_user', null=True, blank=True)
    photo = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher')
    )
    classe = models.ForeignKey(UserLevel, on_delete=models.CASCADE, related_name='class_user', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES) 
    doc = models.ManyToManyField(Document, related_name='user_documents', blank=True)
    
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - ({self.role} - {self.classe.classe if self.classe else 'aucune classe' } - {self.specialization.specialization if self.specialization else 'aucune spécialité'})"

    def save(self, *args, **kwargs):
        if not self.pk or not User.objects.filter(pk=self.pk).exists():
            self.password = make_password(self.password)
        else:
            old_password = User.objects.get(pk=self.pk).password
            if old_password != self.password:
                self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)