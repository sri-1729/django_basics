from django.db import models

# Create your models here.

class users(models.Model):
    user_name = models.CharField(max_length=100)
    motto = models.CharField(max_length=500)
    def __str__(self):
        return self.user_name

