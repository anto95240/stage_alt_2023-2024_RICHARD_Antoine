from django.db import models
from user.models import User

class Document(models.Model):
    ToUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_doc')
    Name = models.CharField(max_length=5100)
    Description = models.CharField(max_length=255)
    FilePath = models.FileField(upload_to='documents/')
    CreatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"{self.Name}"

