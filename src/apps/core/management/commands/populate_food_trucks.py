import csv
from django.core.management.base import BaseCommand

from src.apps.core.models import FoodTruck

FIELDS_MAPPING = {
    "locationid": "location_id",
    "Applicant": "applicant",
    "FacilityType": "facility_type",
    "cnn": "cnn",
    "LocationDescription": "location_description",
    "Address": "address",
    "blocklot": "block_lot",
    "block": "block",
    "lot": "lot",
    "permit": "permit",
    "Status": "status",
    "FoodItems": "food_items",
    "X": "x",
    "Y": "y",
    "Latitude": "latitude",
    "Longitude": "longitude",
    "Schedule": "schedule",
    "dayshours": "days_hours",
    "NOISent": "noi_sent",
    "Approved": "approved",
    "Received": "received",
    "PriorPermit": "prior_permit",
    "ExpirationDate": "expiration_date",
    "Location": "location_info",
    "Fire Prevention Districts": "fire_prevention_districts",
    "Police Districts": "police_districts",
    "Supervisor Districts": "supervisor_districts",
    "Zip Codes": "zip_codes",
    "Neighborhoods (old)": "neighborhoods",
}


class Command(BaseCommand):
    help = "Populate FoodTruck model with data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        csv_path = options["csv_path"]
        food_trucks_to_create = []
        with open(csv_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                mapped_data = {
                    model_field: row[csv_field]
                    for csv_field, model_field in FIELDS_MAPPING.items()
                }
                food_truck = FoodTruck(**mapped_data)
                food_trucks_to_create.append(food_truck)
        batch_size = 100
        FoodTruck.objects.bulk_create(food_trucks_to_create, batch_size=batch_size)
        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
