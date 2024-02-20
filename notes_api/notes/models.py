from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NotesTable(models.Model):
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    note=models.CharField(max_length=1000)
    shared=models.BooleanField(default=False)
    versions=models.TextField(default=[])
    created_at=models.DateTimeField(auto_now_add=True)
