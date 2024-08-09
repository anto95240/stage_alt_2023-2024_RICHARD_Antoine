from django.db import models
from user.models import User, UserLevel, UserSpecialization 
from colorfield.fields import ColorField
    
class Course(models.Model):
    date = models.DateField()
    start_time  = models.TimeField()
    end_time  = models.TimeField()
    subject = models.CharField(max_length=255)
    specialization = models.ForeignKey(UserSpecialization, on_delete=models.CASCADE, related_name='spe_courses')
    class_level = models.ForeignKey(UserLevel, on_delete=models.CASCADE, related_name='class_courses')
    comment = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taught_courses')
    place = models.CharField(max_length=255)
    students = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)
    color = ColorField(default='#FF0000')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"{self.subject} - {self.teacher}"
    
    def get_teacher_name(self):
      return f"{self.teacher.first_name} {self.teacher.last_name} ({self.teacher.role})"
