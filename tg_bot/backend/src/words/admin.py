from django.contrib import admin

from . import models


class WordsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'word', 'translation']
    list_editable = ['word', 'translation']


admin.site.register(models.Words, WordsAdmin)
