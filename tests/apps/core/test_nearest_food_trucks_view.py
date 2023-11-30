from django.contrib.gis.geos import Point
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from src.apps.core.models import FoodTruck


class NearestFoodTrucksViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("nearest-food-trucks")
        FoodTruck.objects.create(
            applicant="Test Truck 1",
            facility_type="Truck",
            location=Point(-118.12345, 34.56789, srid=4326),
        )
        FoodTruck.objects.create(
            applicant="Test Truck 2",
            facility_type="Truck",
            location=Point(-118.13579, 34.54321, srid=4326),
        )
        FoodTruck.objects.create(
            applicant="Test Truck 3",
            facility_type="Truck",
            location=Point(-118.10000, 34.50000, srid=4326),
        )

    def test_get_nearest_food_trucks(self):
        response = self.client.get(
            self.url, {"latitude": 34.56789, "longitude": -118.12345}
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), 3)

    def test_no_food_trucks_available(self):
        FoodTruck.objects.all().delete()

        response = self.client.get(
            self.url, {"latitude": 34.56789, "longitude": -118.12345}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_maximum_number_of_food_trucks(self):
        for i in range(3, 8):
            FoodTruck.objects.create(
                applicant=f"Test Truck {i}",
                facility_type="Truck",
                location=Point(-118.1 + (i * 0.001), 34.5 + (i * 0.001), srid=4326),
            )

        response = self.client.get(
            self.url, {"latitude": 34.56789, "longitude": -118.12345}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
