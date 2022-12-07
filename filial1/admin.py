from django.contrib import admin
from . import models

# admin.site.register(models.User)
admin.site.register(models.Client)
admin.site.register(models.Worker)
admin.site.register(models.Ingridient)
admin.site.register(models.Food)
admin.site.register(models.Order)