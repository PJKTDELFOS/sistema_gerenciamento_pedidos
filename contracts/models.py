from django.db import models
from django.utils import timezone

# Create your models here.


'''
id primarykey
CONTRATANTE-char
ORIGEM-CHAR
PROCESSO,
numero
seguro
apolice
seguradora
VALOR-FLOAT
INICIO-DATE
VIGENCIA-TEXT
FIM-DATE
EXECUTADO-FLOAT
EXECUTAVEL-FLOAT
observações-text

'''
class Contratos (models.Model):
    contratante=models.CharField(max_length=50)
    objeto=models.TextField(max_length=1200)
    origem=models.CharField(max_length=50)
    processo=models.CharField(max_length=50)
    numero=models.CharField(max_length=50)
    seguro=models.BooleanField(default=False, verbose_name=" Seguro")
    apolice=models.CharField(max_length=50, blank=True, null=True, verbose_name="Número da Apólice")
    seguradora = models.CharField(max_length=100, blank=True, null=True, verbose_name="Seguradora")
    inicio=models.DateTimeField()
    vigencia=models.CharField(max_length=50)
    fim_contrato=models.DateTimeField()
    valor_total = models.DecimalField(max_digits=18, decimal_places=2, verbose_name="Valor Total")
    observacoes=models.TextField(max_length=1800)


    def __str__(self):
        return f'{self.contratante} {self.numero}'

    def __str__(self):
        return f"{'Seguro Ativo' if self.seguro else 'Seguro Inativo'}"
#aaa
    def executado(self):
        pedidos = Pedidos.objects.filter(contrato=self)
        total_executado=sum(pedido.valor for pedido in pedidos)
        return total_executado

    def executavel(self):
        return self.valor_total-self.executado()


class Pedidos(models.Model):
    contrato = models.ForeignKey(Contratos, on_delete=models.CASCADE, related_name='pedidos')
    numero=models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrega = models.DateField()



