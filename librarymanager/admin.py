from django.contrib import admin
from . import models

admin.site.register(models.ReservedBook)
admin.site.register(models.RequestedBook)
admin.site.register(models.BurrowedBook)