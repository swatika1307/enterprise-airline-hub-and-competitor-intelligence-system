'''
Airport Lookup Utility
Enterprise Airline Hub & Competitor Intelligence System

Date Started - 16.07.2026
Last Modified - 16.07.2026
'''

import pandas as pd

from config.paths import RAW_FOLDER

def build_airport_lookup():
    airports_df = pd.read_csv(RAW_FOLDER/"dim_airport.csv")
    airport_lookup = {}
    for _, airport in airports_df.iterrows():
        airport_lookup[airport["airport_code"]] = {
            "airport_id" : airport["airport_id"],
            "airport_name" : airport["airport_name"],
            "city" : airport["city"],
            "country" : airport["country"],
            "latitude" : airport["latitude"],
            "longitude" : airport["longitude"],
            "airport_type" : airport["airport_type"],
            "hub_airport" : airport["hub_airport"]
        }
    
    return airport_lookup