'''
Distance Calculator Utility
Enterprise Airline Hub & Competitor Intelligence System

Calculates the great-circle distance between two airports using the Haversine Formula.

Date Started - 16.07.2026
Last Modified - 16.07.2026
'''

from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2

EARTH_RADIUS = 6371

def calculate_distance(origin_lat, origin_lon, destination_lat, destination_lon):
    # Convert degrees to radians
    origin_lat = radians(origin_lat)
    origin_lon = radians(origin_lon)
    destination_lat = radians(destination_lat)
    destination_lon = radians(destination_lon)

    # Difference
    delta_lat = destination_lat - origin_lat
    delta_lon = destination_lon - origin_lon

    # Haversine formula
    a = (sin(delta_lat / 2) ** 2 + cos(origin_lat) * cos(destination_lat) * sin(delta_lon / 2) ** 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = EARTH_RADIUS * c

    return round(distance, 2)