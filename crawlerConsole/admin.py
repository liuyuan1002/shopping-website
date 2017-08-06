from django.contrib import admin
from crawlerConsole import models
# Register your models here.

class pcListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'processName','host,' 'path']

admin.register(models.pcList,pcListAdmin)