# Django
from django.db import models

class Profile(models.Model):
    # Modelo del Perfil que amplía la información del Usuario de Django

    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        # Retorna el username
        return self.name

