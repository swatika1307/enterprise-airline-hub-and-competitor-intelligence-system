'''
Generate Aircraft Fleet Master
Enterprise Airline Hub & Competitor Intelligence System

Date Started - 16.07.2026
Last Modified - 16.07.2026
'''

import random
import pandas as pd

from config.paths import RAW_FOLDER
from config.config import PROJECT_YEAR

from config.constants import (
    SIMULATED_FLEET,
    REGISTRATION_PREFIX,
    AIRLINE_AIRCRAFT_MODELS,
    AIRCRAFT_MODEL_CONFIG
)

from utils.registration_generator import generate_registration

def generate_aircraft():
    airlines_df = pd.read_csv(RAW_FOLDER/"dim_airline.csv")

    aircraft_records = []

    aircraft_id = 1

    for _, airline in airlines_df.iterrows():
        airline_name = airline["airline_name"]
        airline_id = airline["airline_id"]
        prefix = REGISTRATION_PREFIX[airline_name]
        fleet_count = SIMULATED_FLEET[airline_name]
        available_models = AIRLINE_AIRCRAFT_MODELS[airline_name]
        for number in range(1, fleet_count + 1):
            model = random.choice(available_models)
            model_config  = AIRCRAFT_MODEL_CONFIG[model]
            manufacturer = model_config["manufacturer"]
            family = model_config["family"]
            seating_capacity = model_config["seating_capacity "]
            manufacture_year = random.randint(
                model_config["introduced_year"],
                PROJECT_YEAR - 1
            )
            aircraft_age = PROJECT_YEAR - manufacture_year
            fuel_efficiency = round(
                random.uniform(*model_config["fuel_efficiency_range"]),
                2
            )
            aircraft_status = random.choices(
                ["Active", "Maintenance"],
                weights=[95, 5]
            )[0]
            aircraft_records.append({
                "aircraft_id": aircraft_id,
                "airline_id": airline_id,
                "airline_name": airline_name,
                "registration_number": generate_registration(prefix, number),
                "manufacturer": manufacturer,
                "aircraft_model": model,
                "aircraft_family": family,
                "seating_capacity": seating_capacity ,
                "manufacture_year": manufacture_year,
                "aircraft_age": aircraft_age,
                "fuel_efficiency": fuel_efficiency,
                "aircraft_status": aircraft_status
            })
            aircraft_id += 1

    df = pd.DataFrame(aircraft_records)

    output_path = RAW_FOLDER / "dim_aircraft.csv"

    df.to_csv(output_path, index=False)

    print("=" * 60)
    print("AIRCRAFT MASTER GENERATED")
    print("=" * 60)

    print(df.head())

    print(f"\nTotal Aircraft : {len(df)}")

    print(f"\nSaved Successfully!\n{output_path}")

    return df