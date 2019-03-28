from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class List(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    description     = models.CharField(max_length=255)
    is_completed    = models.BooleanField(default=False)
    is_checked      = models.BooleanField(default=False)

    def __str__(self):
        return self.description

