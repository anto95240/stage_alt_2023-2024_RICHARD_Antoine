from django.db import models
from user.models import User, UserLevel, UserSpecialization 
    
class Note(models.Model):
    note = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Note")
    coefficient = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Coefficient")
    subject = models.CharField(max_length=255, verbose_name="Matière")
    specialization = models.ForeignKey(UserSpecialization, on_delete=models.CASCADE, related_name='spe_note', verbose_name="Spécialisation")
    class_level = models.ForeignKey(UserLevel, on_delete=models.CASCADE, related_name='class_note', verbose_name="Niveau de classe")
    label = models.TextField(null=True, blank=True, verbose_name="Étiquette")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taught_note', verbose_name="Enseignant")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrolled_note', blank=True, verbose_name="Étudiants")
    total_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Noté sur")
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.subject} - {self.note}"
    
    def get_teacher_name(self):
      return f"{self.teacher.first_name} {self.teacher.last_name} ({self.teacher.role})"

    def calculate_total_score(self):
        if self.note and self.coefficient:
            self.total_score = self.note * self.coefficient
            self.save()
        else:
            self.total_score = None
            self.save()
        return self.total_score