from django.db import models
from django.conf import settings
from django.utils.timezone import now
# Create your models here.

class Task(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name        = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    pub_date    = models.DateField(null=True,default=now)
    conc_date   = models.DateField(null=True,)
    concluded   = models.BooleanField(null=True,default=False)

    def __str__(self) -> str:
        return self.name