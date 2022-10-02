from django.contrib import admin
from . import models
# Register your models here.
from .models import Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','status','slug','author')
admin.site.register(models.Post,AuthorAdmin)