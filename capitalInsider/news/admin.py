from django.contrib import admin
from . import models

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'date']
    list_filter = ['name', 'date']


admin.site.register(models.News)
admin.site.register(models.Comment, CommentAdmin)

