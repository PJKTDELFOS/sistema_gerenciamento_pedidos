from django.db import models
from django.utils import timezone

# Create your models here.

'''
id-primarey key, orgão-text,numero-text,
datadisputa-date,modalidde-text,
status-text,descrição-text
'''

class processo(models.Model):
    orgao=models.CharField(max_length=100)
    numero=models.CharField(max_length=15)
    data=models.DateTimeField()
    modalidade=models.CharField(max_length=100)
    status=models.CharField(max_length=10)
    objeto=models.TextField(max_length=1800)
    descrição=models.TextField(max_length=1800)

    def __str__(self):
        return f'{self.orgao}'


