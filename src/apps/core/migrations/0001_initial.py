# Generated by Django 4.2.7 on 2023-11-30 02:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FoodTruck",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location_id", models.CharField(max_length=255)),
                ("applicant", models.CharField(max_length=255)),
                ("facility_type", models.CharField(max_length=255)),
                ("cnn", models.CharField(max_length=255)),
                ("location_description", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("block_lot", models.CharField(max_length=255)),
                ("block", models.CharField(max_length=255)),
                ("lot", models.CharField(max_length=255)),
                ("permit", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
                ("food_items", models.CharField(max_length=2048)),
                ("x", models.CharField(max_length=255)),
                ("y", models.CharField(max_length=255)),
                ("latitude", models.CharField(max_length=255)),
                ("longitude", models.CharField(max_length=255)),
                ("schedule", models.CharField(max_length=255)),
                ("days_hours", models.CharField(max_length=255)),
                ("noi_sent", models.CharField(max_length=255)),
                ("approved", models.CharField(max_length=255)),
                ("received", models.CharField(max_length=255)),
                ("prior_permit", models.CharField(max_length=255)),
                ("expiration_date", models.CharField(max_length=255)),
                ("location", django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ("fire_prevention_districts", models.CharField(max_length=255)),
                ("police_districts", models.CharField(max_length=255)),
                ("supervisor_districts", models.CharField(max_length=255)),
                ("zip_codes", models.CharField(max_length=255)),
                ("neighborhoods", models.CharField(max_length=255)),
            ],
        ),
    ]
