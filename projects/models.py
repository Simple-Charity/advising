from django.db import models
from analyst.models import *

class Project(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
