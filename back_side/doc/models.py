from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"{self.name}"

