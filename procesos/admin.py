from django.contrib import admin

# Register your models here.

from procesos import models

@admin.register(models.processo)
class processoadmin(admin.ModelAdmin):
    list_display = ('id','orgao','numero','data','modalidade','data','valor',)
    ordering = ('-id',)
    search_fields = ('orgao','numero','descrição','modalidade')