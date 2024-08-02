from django.db import models
from user.models import User, UserLevel, UserSpecialization 
from colorfield.fields import ColorField
    
class Course(models.Model):
    Date = models.DateField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Subject = models.CharField(max_length=255)
    Specialization = models.ForeignKey(UserSpecialization, on_delete=models.CASCADE, related_name='spe_courses')
    ClassLevel = models.ForeignKey(UserLevel, on_delete=models.CASCADE, related_name='class_courses')
    Comment = models.TextField(null=True, blank=True)
    Teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taught_courses')
    Place = models.CharField(max_length=255)
    Students = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)
    Color = ColorField(default='#FF0000')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"{self.Subject} - {self.Teacher}"
    
    def get_teacher_name(self):
      return f"{self.Teacher.FirstName} {self.Teacher.LastName} ({self.Teacher.Role})"
