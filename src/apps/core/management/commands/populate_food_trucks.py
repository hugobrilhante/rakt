import csv
from django.core.management.base import BaseCommand

from src.apps.core.models import FoodTruck

# Mapping between CSV column names and model field names
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
    "Location": "location",
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

    # Define the main logic of the command to handle the CSV data
    def handle(self, *args, **options):
        # Retrieve the path to the CSV file provided as a command-line argument
        csv_path = options["csv_path"]

        # Open the CSV file and read its contents as a dictionary
        with open(csv_path, "r") as file:
            # Use DictReader to read the CSV file as a dictionary
            reader = csv.DictReader(file)

            # Iterate through each row in the CSV file
            for row in reader:
                # Map CSV column names to model field names using the defined mapping
                mapped_data = {
                    model_field: row[csv_field]
                    for csv_field, model_field in FIELDS_MAPPING.items()
                }

                # Create a new FoodTruck object using the mapped data and save it to the database
                FoodTruck.objects.create(**mapped_data)

        # Display a success message after importing the data
        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
