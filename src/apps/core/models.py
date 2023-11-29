from django.db import models


class FoodTruck(models.Model):
    location_id = models.CharField(max_length=255)
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=255)
    cnn = models.CharField(max_length=255)
    location_description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    block_lot = models.CharField(max_length=255)
    block = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    permit = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    food_items = models.CharField(max_length=2048)
    x = models.CharField(max_length=255)
    y = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    days_hours = models.CharField(max_length=255)
    noi_sent = models.CharField(max_length=255)
    approved = models.CharField(max_length=255)
    received = models.CharField(max_length=255)
    prior_permit = models.CharField(max_length=255)
    expiration_date = models.CharField(max_length=255)
    location_info = models.CharField(max_length=255)
    fire_prevention_districts = models.CharField(max_length=255)
    police_districts = models.CharField(max_length=255)
    supervisor_districts = models.CharField(max_length=255)
    zip_codes = models.CharField(max_length=255)
    neighborhoods = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.facility_type} - {self.latitude}, {self.longitude} "
