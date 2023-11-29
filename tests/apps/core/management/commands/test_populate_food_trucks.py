import os.path
from pathlib import Path

from django.core.management import call_command
from django.test import TestCase

from src.apps.core.models import FoodTruck

BASE_DIR = Path(__file__).resolve().parent


class PopulateFoodTrucksCommandTest(TestCase):
    def setUp(self):
        self.csv_file_path = os.path.join(BASE_DIR, "food-truck-data-test.csv")

    def test_populate_food_trucks_command(self):
        call_command("populate_food_trucks", self.csv_file_path)
        expected_number_of_objects = 5
        self.assertEqual(FoodTruck.objects.count(), expected_number_of_objects)

    def tearDown(self):
        FoodTruck.objects.all().delete()
