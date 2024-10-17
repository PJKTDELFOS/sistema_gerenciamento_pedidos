from django.db import models
from django.utils import timezone
from decimal import Decimal

# Create your models here.

'''
id-primarey key, orgão-text,numero-text,
datadisputa-date,modalidde-text,
status-text,descrição-text
'''

class processo(models.Model):
    orgao=models.CharField(max_length=100,null=True)
    numero=models.CharField(max_length=15,null=True)
    data=models.DateTimeField()
    modalidade=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=10,null=True)
    objeto=models.TextField(max_length=1800,null=True)
    descrição=models.TextField(max_length=1800,null=True)
    valor=models.DecimalField(max_digits=18, decimal_places=2,default=0.00,null=True,)

    def __str__(self):
        return f'{self.orgao}'


