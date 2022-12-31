from django.contrib import admin
from core.admin import UserAdmin
from . import models

# # Register your models here.
admin.site.register(models.Job)
admin.site.register(models.Section)
