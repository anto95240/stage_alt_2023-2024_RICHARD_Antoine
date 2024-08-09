from django.db import models
from user.models import User

class Presence(models.Model):
    student = models.ManyToManyField(User, related_name='presences')
    is_abscent = models.BooleanField(default=False)
    is_late = models.BooleanField(default=False)
    late_duration_choices = [
        (5, '5 minutes'),
        (10, '10 minutes'),
        (15, '15 minutes'),
        (20, '20 minutes'),
    ]
    late_duration = models.IntegerField(choices=late_duration_choices, null=True, blank=True)
    date = models.DateField()
    absence_start_time = models.TimeField(null=True, blank=True)
    absence_end_time = models.TimeField(null=True, blank=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        students_names = ", ".join([f"{student.first_name} {student.last_name}" for student in self.Student.all()])
        if self.IsAbscent :
            return  f"{students_names} - absent le {self.date} de {self.absence_start_time} à {self.absence_end_time}"
        elif self.IsLate :
            return  f"{students_names} - retard de {self.late_duration} minutes, le {self.date}"
        else:
            return students_names

    def save(self, *args, **kwargs):
        if not self.is_abscent:
            self.absence_start_time = None
            self.absence_end_time = None
        if not self.is_late:
            self.late_duration = None
        super().save(*args, **kwargs)