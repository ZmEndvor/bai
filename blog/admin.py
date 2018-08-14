from django.contrib import admin
from  .models import Lunbo

# Register your models here.

@admin.register(Lunbo)
class LunboAdmin(admin.ModelAdmin):
    list_display = ("id","img","text","chooes")
    ordering = ["id", ]