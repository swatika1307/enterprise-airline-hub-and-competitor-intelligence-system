'''
Project Constants

Date Started - 15.07.2026
Last Modified - 21.07.2026
'''

AIRCRAFT_MANUFACTURERS = [
    "Airbus",
    "Boeing"
]

LOYALTY_TIERS = [
    "Silver",
    "Gold",
    "Platinum"
]

BOOKING_CHANNELS = [
    "Website",
    "Mobile App",
    "Travel Agency",
    "OTA"
]

CABIN_CLASSES = [
    "Economy",
    "Premium Economy",
    "Business",
    "First"
]

FLIGHT_TYPES = [
    "Domestic",
    "International"
]

# -------------------------------------
# STEP 2.4 - AIRCRAFT FLEET GENERATION
# -------------------------------------
SIMULATED_FLEET = {
    "IndiGo": 35,
    "Air India": 30,
    "Akasa Air": 15,
    "Emirates": 30,
    "Singapore Airlines": 25,
    "Qatar Airways": 25
}

REGISTRATION_PREFIX = {
    "IndiGo": "VT",
    "Air India": "AI",
    "Akasa Air": "AK",
    "Emirates": "A6",
    "Singapore Airlines": "9V",
    "Qatar Airways": "A7"
}

AIRLINE_AIRCRAFT_MODELS = {
    "IndiGo": [
        "A320neo",
        "A321neo"
    ],
    "Air India": [
        "A320neo",
        "A350-900",
        "B787-8 Dreamliner",
        "B777-300ER"
    ],
    "Akasa Air": [
        "B737 MAX 8"
    ],
    "Emirates": [
        "A350-900",
        "B777-300ER"
    ],
    "Singapore Airlines": [
        "A350-900",
        "B787-8 Dreamliner"
    ],
    "Qatar Airways": [
        "A350-900",
        "B787-8 Dreamliner",
        "B777-300ER"
    ]
}

AIRCRAFT_MODEL_CONFIG = {
    "A320neo": {
        "manufacturer": "Airbus",
        "family": "Narrow Body",
        "seating_capacity ": 186,
        "introduced_year": 2016,
        "fuel_efficiency_range": (4.0, 4.4)
    },
    "A321neo": {
        "manufacturer": "Airbus",
        "family": "Narrow Body",
        "seating_capacity ": 232,
        "introduced_year": 2017,
        "fuel_efficiency_range": (3.8, 4.2)
    },
    "A350-900": {
        "manufacturer": "Airbus",
        "family": "Wide Body",
        "seating_capacity ": 320,
        "introduced_year": 2015,
        "fuel_efficiency_range": (3.3, 3.7)
    },
    "B737 MAX 8": {
        "manufacturer": "Boeing",
        "family": "Narrow Body",
        "seating_capacity ": 197,
        "introduced_year": 2017,
        "fuel_efficiency_range": (3.9, 4.3)
    },
    "B787-8 Dreamliner": {
        "manufacturer": "Boeing",
        "family": "Wide Body",
        "seating_capacity ": 290,
        "introduced_year": 2012,
        "fuel_efficiency_range": (3.2, 3.6)
    },
    "B777-300ER": {
        "manufacturer": "Boeing",
        "family": "Wide Body",
        "seating_capacity ": 360,
        "introduced_year": 2005,
        "fuel_efficiency_range": (2.8, 3.2)
    }
}

# -------------------------------
# STEP 2.5 - ROUTE CONFIGURATION
# -------------------------------
AIRLINE_HUBS = {
    "IndiGo" : "DEL",
    "Air India" : "DEL",
    "Akasa Air" : "BOM",
    "Emirates" : "DXB",
    "Singapore Airlines" : "SIN",
    "Qatar Airways" : "DOH"
}

AVERAGE_CRUISING_SPEED = 820 # in km/hr

GROUND_OPERATION_TIME = 30 # in minutes

TOTAL_NETWORK_ROUTES = 120

ROUTE_DISTRIBUTION = {
    "domestic": 0.40,
    "india_international": 0.40,
    "international": 0.20
}

AIRLINES_PER_ROUTE = {
    "minimum": 1,
    "maximum": 3
}

AIRLINE_ROUTE_RULES = {
    "IndiGo" : {
        "Domestic" : True,
        "India-International" : True,
        "International" : False
    },
    "Air India" : {
        "Domestic" : True,
        "India-International" : True,
        "International" : False
    },
    "Akasa Air" : {
        "Domestic" : True,
        "India-International" : True,
        "International" : False
    },
    "Emirates" : {
        "Domestic" : False,
        "India-International" : True,
        "International" : True
    },
    "Singapore Airlines" : {
        "Domestic" : False,
        "India-International" : True,
        "International" : True
    },
    "Qatar Airways" : {
        "Domestic" : False,
        "India-International" : True,
        "International" : True
    }
}

# ----------------------------------------
# STEP 2.7 - FLIGHT OPERATIONS GENERATION
# ----------------------------------------
ROUTE_DEMAND_RANGES = {
    "High" : (10, 18),
    "Medium" : (6, 10),
    "Low" : (2, 5)
}

SEASON_MULTIPLIER = {
    "Peak" : 1.20,
    "Regular" : 1.00,
    "Off-Peak" : 0.80
}

WEEKEND_MULTIPLIER = 1.10

DEPARTURE_WAVES = {
    "Red Eye" : {
        "start_hour" : "00:00",
        "end_hour" : "04:59",
        "departure_weight " : 5
    },
    "Morning Peak" : {
        "start_hour" : "05:00",
        "end_hour" : "07:59",
        "departure_weight " : 30
    },
    "Morning" : {
        "start_hour" : "08:00",
        "end_hour" : "10:59",
        "departure_weight " : 20
    },
    "Afternoon" : {
        "start_hour" : "11:00",
        "end_hour" : "15:59",
        "departure_weight " : 10
    },
    "Evening Peak" : {
        "start_hour" : "16:00",
        "end_hour" : "20:59",
        "departure_weight " : 30
    },
    "Night" : {
        "start_hour" : "21:00",
        "end_hour" : "23:59",
        "departure_weight " : 10
    }
}

MIN_TURNAROUND_TIME = 45
MAX_TURNAROUND_TIME = 90

MIN_FLIGHT_NUMBER = 1000
MAX_FLIGHT_NUMBER = 9999

DEFAULT_FLIGHT_STATUS = "Scheduled"