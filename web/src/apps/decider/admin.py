from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models import fields
from . import models 

@admin.register(models.Site)
class SiteAdmin(admin.ModelAdmin):
    list_filter = ('url',)
    list_display = ('url',  'created_at', 'updated_at' )
    fields = ('url', )
    search_fields = ['url',]
    
@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('url', 'mood', 'user', 'status', 'updated_at', 'created_at')
    fields = ('url', 'user', 'status', 'mood' )
    search_fields = ['status',]
    