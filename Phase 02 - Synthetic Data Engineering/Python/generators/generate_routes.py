'''
Generate Route Master
Enterprise Airline Hub & Competitor Intelligence System

Date Started - 16.07.2026
Last Modified - 16.07.2026
'''

import random
import pandas as pd

from config.paths import RAW_FOLDER

from config.constants import (
    TOTAL_NETWORK_ROUTES,
    ROUTE_DISTRIBUTION,
    AVERAGE_CRUISING_SPEED,
    GROUND_OPERATION_TIME,
    AIRLINE_HUBS
)

from utils.airport_lookup import build_airport_lookup
from utils.distance_calculator import calculate_distance


def generate_routes():
    airport_lookup = build_airport_lookup()
    indian_airports = [
        code
        for code, airport in airport_lookup.items()
        if airport["country"] == "India"
    ]
    international_airports = [
        code
        for code, airport in airport_lookup.items()
        if airport["country"] != "India"
    ]
    # -----------------------
    # WEIGHTED AIRPORT POOLS
    # -----------------------
    major_indian_hubs = [
        "DEL",
        "BOM",
        "BLR",
        "HYD",
        "MAA"
    ]
    major_international_hubs = [
        "DXB",
        "SIN",
        "DOH",
        "LHR",
        "JFK"
    ]
    weighted_indian_airports = (
        indian_airports
        + major_indian_hubs * 3
    )
    weighted_international_airports = (
        international_airports
        + major_international_hubs * 3
    )
    route_records = []
    existing_routes = set()
    route_id = 1
    # ---------------------------------------
    # CALCULATE NUMBER OF ROUTES BY CATEGORY
    # ---------------------------------------
    domestic_routes = int(
        TOTAL_NETWORK_ROUTES *
        ROUTE_DISTRIBUTION["domestic"]
    )
    india_international_routes = int(
        TOTAL_NETWORK_ROUTES *
        ROUTE_DISTRIBUTION["india_international"]
    )
    international_routes = (
        TOTAL_NETWORK_ROUTES
        - domestic_routes
        - india_international_routes
    )


    # ----------------
    # HELPER FUNCTION
    # ----------------
    def add_route(origin, destination, route_type):
        nonlocal route_id
        if origin == destination:
            return False
        unique_route = (origin, destination)
        if unique_route in existing_routes:
            return False
        existing_routes.add(unique_route)
        origin_airport = airport_lookup[origin]
        destination_airport = airport_lookup[destination]
        distance_km = calculate_distance(
            origin_airport["latitude"],
            origin_airport["longitude"],
            destination_airport["latitude"],
            destination_airport["longitude"]
        )
        estimated_duration_min = round(
            (distance_km / AVERAGE_CRUISING_SPEED) * 60
            + GROUND_OPERATION_TIME
        )
        hub_airports = set(AIRLINE_HUBS.values())
        is_hub_route = (
            origin in hub_airports
            or
            destination in hub_airports
        )
        route_records.append({
            "route_id": route_id,
            "origin_airport": origin,
            "destination_airport": destination,
            "distance_km": round(distance_km, 2),
            "estimated_duration_min": estimated_duration_min,
            "route_type": route_type,
            "is_hub_route": is_hub_route
        })
        route_id += 1
        return True
    
    # -------------------------
    # GENERATE DOMESTIC ROUTES
    # -------------------------
    while len([
        r for r in route_records
        if r["route_type"] == "Domestic"
    ]) < domestic_routes:
        add_route(
            random.choice(weighted_indian_airports),
            random.choice(weighted_indian_airports),
            "Domestic"
        )
    # --------------------------------------
    # GENERATE INDIA - INTERNATIONAL ROUTES
    # --------------------------------------
    while len([
        r for r in route_records
        if r["route_type"] == "India-International"
    ]) < india_international_routes:
        add_route(
            random.choice(weighted_indian_airports),
            random.choice(weighted_international_airports),
            "India-International"
        )
    # ------------------------------
    # GENERATE INTERNATIONAL ROUTES
    # ------------------------------
    while len([
        r for r in route_records
        if r["route_type"] == "International"
    ]) < international_routes:
        add_route(
            random.choice(weighted_international_airports),
            random.choice(weighted_international_airports),
            "International"
        )

    # -----------------
    # CREATE DATAFRAME
    # -----------------
    df = pd.DataFrame(route_records)
    # -----------
    # VALIDATION
    # -----------
    assert not df.empty, "Route dataset is empty."
    assert (
        df["origin_airport"] !=
        df["destination_airport"]
    ).all(), "Origin and Destination cannot be same."
    assert not df.duplicated(
        subset=[
            "origin_airport",
            "destination_airport"
        ]
    ).any(), "Duplicate routes detected."
    # -------
    # EXPORT
    # -------
    output_path = RAW_FOLDER / "dim_route.csv"
    df.to_csv(
        output_path,
        index=False
    )

    print("=" * 60)
    print("ROUTE MASTER GENERATED")
    print("=" * 60)

    print(df.head())

    print(f"\nTotal Routes : {len(df)}")

    print(f"\nSaved Successfully!\n{output_path}")

    return df