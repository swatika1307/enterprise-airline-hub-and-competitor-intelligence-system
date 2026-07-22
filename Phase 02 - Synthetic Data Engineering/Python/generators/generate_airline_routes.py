"""
Generate Airline Route Bridge
Enterprise Airline Hub & Competitor Intelligence System

Date Started  : 19.07.2026
Last Modified : 19.07.2026
"""

import random
import pandas as pd

from config.paths import RAW_FOLDER
from config.constants import AIRLINE_ROUTE_RULES


def generate_airline_routes():
    airline_df = pd.read_csv(RAW_FOLDER / "dim_airline.csv")
    routes_df = pd.read_csv(RAW_FOLDER / "dim_route.csv")
    bridge_records = []
    bridge_id = 1
    # ------------------------
    # GENERATE BRIDGE RECORDS
    # ------------------------
    for _, route in routes_df.iterrows():
        route_id = route["route_id"]
        route_type = route["route_type"]
        origin = route["origin_airport"]
        destination = route["destination_airport"]
        eligible_airlines = []
        for _, airline in airline_df.iterrows():
            airline_id = airline["airline_id"]
            airline_name = airline["airline_name"]
            rules = AIRLINE_ROUTE_RULES[airline_name]
            # Route Eligibility Check
            if not rules[route_type]:
                continue
            # Foreign Airline Hub Restrictions
            if airline_name == "Emirates":
                if "DXB" not in [origin, destination]:
                    continue
            elif airline_name == "Singapore Airlines":
                if "SIN" not in [origin, destination]:
                    continue
            elif airline_name == "Qatar Airways":
                if "DOH" not in [origin, destination]:
                    continue
            eligible_airlines.append({
                "airline_id": airline_id,
                "airline_name": airline_name
            })
        # --------------------------------------
        # SKIP IF NO AIRLINE OPERATES THE ROUTE
        # --------------------------------------
        if not eligible_airlines:
            continue
        # ----------------
        # DOMESTIC ROUTES
        # ----------------
        if route_type == "Domestic":
            selected_count = random.randint(
                min(2, len(eligible_airlines)),
                len(eligible_airlines)
            )
            selected_airlines = random.sample(
                eligible_airlines,
                selected_count
            )
        # ----------------------
        # INDIA - INTERNATIONAL
        # ----------------------
        elif route_type == "India-International":
            selected_count = random.randint(
                min(2, len(eligible_airlines)),
                len(eligible_airlines)
            )
            selected_airlines = random.sample(
                eligible_airlines,
                selected_count
            )
        # --------------
        # INTERNATIONAL
        # --------------
        else:
            selected_airlines = eligible_airlines
        # ----------------------
        # CREATE BRIDGE RECORDS
        # ----------------------
        for airline in selected_airlines:
            bridge_records.append({
                "bridge_id": bridge_id,
                "airline_id": airline["airline_id"],
                "airline_name": airline["airline_name"],
                "route_id": route_id
            })
            bridge_id += 1

    df = pd.DataFrame(bridge_records)

    output_path = RAW_FOLDER / "bridge_airline_route.csv"

    df.to_csv(output_path, index=False)

    print("=" * 60)
    print("BRIDGE AIRLINE ROUTE MASTER")
    print("=" * 60)

    print(df.head())

    print(f"\nTotal Records : {len(df)}")

    print(f"\nSaved Successfully!\n{output_path}")

    return df