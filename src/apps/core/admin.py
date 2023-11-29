from django.contrib import admin
from .models import FoodTruck


@admin.register(FoodTruck)
class FoodTruckAdmin(admin.ModelAdmin):
    list_display = ["applicant", "facility_type", "status", "location_id"]
    list_filter = ["facility_type", "status"]
    search_fields = ["applicant", "location_id", "food_items"]
