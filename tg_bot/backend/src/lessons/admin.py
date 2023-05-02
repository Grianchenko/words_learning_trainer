from django.contrib import admin

from . import models


class LessonsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'theme', 'date', 'homework', 'mark']
    list_editable = ['theme', 'date', 'homework', 'mark']


admin.site.register(models.Lessons, LessonsAdmin)
