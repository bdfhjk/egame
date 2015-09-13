from django.contrib import admin

from .models import Building, BuildingState

admin.site.register(Building)
admin.site.register(BuildingState)
