from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

class Jobs(models.Model):
    company = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    required_skills = models.TextField()
    open = models.BooleanField(default=True)

    class Meta:
        ordering = ('-id',)