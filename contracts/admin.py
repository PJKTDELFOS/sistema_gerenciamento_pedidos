from django.contrib import admin
from django.db import models

from django import forms
from .models import Contratos,Pedidos
# Register your models here.

class Pedidoinline(admin.TabularInline):
    model = Pedidos
    extra=1

@admin.register(Contratos)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id','contratante','origem','processo','numero',
                    'seguro','apolice','seguradora','valor_total','inicio',
                    'vigencia','fim_contrato','executado','executavel')
    ordering = ('-id',)
    inlines = [Pedidoinline]
    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'disabled': False})},  # Corrigido o uso de CharField
    }

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is not None and not obj.seguro:
            form.base_fields['apolice'].widget.attrs['disabled'] = True
            form.base_fields['seguradora'].widget.attrs['disabled'] = True
        return form


@admin.register(Pedidos)
class Pedidoadmin(admin.ModelAdmin):
    list_display = ('contrato','numero','valor','data_entrega')
    ordering = ('id',)




