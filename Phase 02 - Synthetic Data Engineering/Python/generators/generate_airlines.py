'''
Generate Airline Master Table
Enterprise Airline Hub & Competitor Intelligence System

Date Started - 15.07.2026
Last Modified - 15.07.2026
'''

import pandas as pd

from config.paths import RAW_FOLDER

def generate_airlines():
    airlines = [
        {
            "airline_id" : 1,
            "airline_code" : "6E",
            "airline_name" : "IndiGo",
            "country" : "India",
            "headquarters" : "Gurugram",
            "airline_type" : "Low Cost",
            "alliance" : "None",
            "hub_airport" : "DEL",
            "founded_year" : 2006,
            "real_world_fleet_size" : 420,
            "is_active" : True 
        },
        {
            "airline_id" : 2,
            "airline_code" : "AI",
            "airline_name" : "Air India",
            "country" : "India",
            "headquarters" : "Gurugram",
            "airline_type" : "Full Service",
            "alliance" : "Star Alliance",
            "hub_airport" : "DEL",
            "founded_year" : 1932,
            "real_world_fleet_size" : 215,
            "is_active" : True
        },
        {
            "airline_id" : 3,
            "airline_code" : "QP",
            "airline_name" : "Akasa Air",
            "country" : "India",
            "headquarters" : "Mumbai",
            "airline_type" : "Low Cost",
            "alliance" : "None",
            "hub_airport" : "BOM",
            "founded_year" : 2021,
            "real_world_fleet_size" : 35,
            "is_active" : True
        },
        {
            "airline_id" : 4,
            "airline_code" : "EK",
            "airline_name" : "Emirates",
            "country" : "United Arab Emirates",
            "headquarters" : "Dubai",
            "airline_type" : "Full Service",
            "alliance" : "None",
            "hub_airport" : "DXB",
            "founded_year" : 1985,
            "real_world_fleet_size" : 260,
            "is_active" : True
        },
        {
            "airline_id" : 5,
            "airline_code" : "SQ",
            "airline_name" : "Singapore Airlines",
            "country" : "Singapore",
            "headquarters" : "Singapore",
            "airline_type" : "Full Service",
            "alliance" : "Star Alliance",
            "hub_airport" : "SIN",
            "founded_year" : 1972,
            "real_world_fleet_size" : 200,
            "is_active" : True
        },
        {
            "airline_id" : 6,
            "airline_code" : "QR",
            "airline_name" : "Qatar Airways",
            "country" : "Qatar",
            "headquarters" : "Doha",
            "airline_type" : "Full Service",
            "alliance" : "Oneworld",
            "hub_airport" : "DOH",
            "founded_year" : 1993,
            "real_world_fleet_size" : 250,
            "is_active" : True
        }
    ]

    df = pd.DataFrame(airlines)

    output_path = RAW_FOLDER/"dim_airline.csv"

    df.to_csv(output_path, index = False)

    print("=" * 60)
    print("AIRLINE MASTER GENERATED")
    print("=" * 60)

    print(df)

    print("\nSaved Succesfully!")

    print(output_path)