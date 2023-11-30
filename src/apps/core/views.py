from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodTruck
from .serializers import FoodTruckSerializer


class NearestFoodTrucksView(APIView):
    def get(self, request):
        try:
            # Extract latitude and longitude from the query parameters
            latitude = float(request.query_params.get("latitude"))
            longitude = float(request.query_params.get("longitude"))

            food_trucks = (
                FoodTruck.objects.filter(
                    facility_type="Truck"  # Filter condition for facility_type equal to 'Truck'
                )
                .annotate(
                    distance=Distance(
                        "location", Point(longitude, latitude, srid=4326)
                    )  # Calculate distance
                )
                .order_by("distance")[:5]
            )  # Retrieve the five closest food trucks

            # Serialize the retrieved food truck objects
            serializer = FoodTruckSerializer(food_trucks, many=True)

            # Return the serialized data as a JSON response
            return Response(serializer.data)

        except (TypeError, ValueError):
            # Catch exceptions if the latitude or longitude provided are invalid
            return Response({"error": "Invalid coordinates"}, status=400)
