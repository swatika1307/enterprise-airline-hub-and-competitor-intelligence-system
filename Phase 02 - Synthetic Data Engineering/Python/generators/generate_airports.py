'''
Generate Airport Master Table
Enterprise Airline Hub & Competitor Intelligence System

Date Started - 15.07.2026
Last Modified - 16.07.2026
'''

import pandas as pd

from config.paths import RAW_FOLDER

def generate_airports():
    airports = [
        # ------
        # INDIA
        # ------
        (1, "DEL", "Indira Gandhi International Airport", "Delhi", "Delhi", "India", 28.5562, 77.1000, "International", True),
        (2, "BOM", "Chhatrapati Shivaji Maharaj International Airport", "Mumbai", "Maharashtra", "India", 19.0896, 72.8656, "International", True),
        (3, "BLR", "Kempegowda International Airport", "Bengaluru", "Karnataka", "India", 13.1986, 77.7066, "International", False),
        (4, "HYD", "Rajiv Gandhi International Airport", "Hyderabad", "Telangana", "India", 17.2403, 78.4294, "International", False),
        (5, "MAA", "Chennai International Airport", "Chennai", "Tamil Nadu", "India", 12.9941, 80.1709, "International", False),
        (6, "CCU", "Netaji Subhas Chandra Bose International Airport", "Kolkata", "West Bengal", "India", 22.6547, 88.4467, "International", False),
        (7, "COK", "Cochin International Airport", "Kochi", "Kerala", "India", 10.1520, 76.4019, "International", False),
        (8, "AMD", "Sardar Vallabhbhai Patel International Airport", "Ahmedabad", "Gujarat", "India", 23.0734, 72.6266, "International", False),
        (9, "PNQ", "Pune Airport", "Pune", "Maharashtra", "India", 18.5822, 73.9197, "Domestic", False),
        (10, "GOX", "Manohar International Airport", "Goa", "Goa", "India", 15.7293, 73.9284, "International", False),
        (11, "JAI", "Jaipur International Airport", "Jaipur", "Rajasthan", "India", 26.8242, 75.8122, "International", False),
        (12, "LKO", "Chaudhary Charan Singh International Airport", "Lucknow", "Uttar Pradesh", "India", 26.7606, 80.8893, "International", False),
        (13, "GAU", "Lokpriya Gopinath Bordoloi International Airport", "Guwahati", "Assam", "India", 26.1061, 91.5859, "International", False),
        (14, "SXR", "Srinagar Airport", "Srinagar", "Jammu & Kashmir", "India", 33.9871, 74.7742, "Domestic", False),
        (15, "TRV", "Trivandrum International Airport", "Thiruvananthapuram", "Kerala", "India", 8.4821, 76.9201, "International", False),
        # --------------
        # INTERNATIONAL
        # --------------
        (16, "DXB", "Dubai International Airport", "Dubai", "Dubai", "United Arab Emirates", 25.2532, 55.3657, "International", True),
        (17, "SIN", "Singapore Changi Airport", "Singapore", "Singapore", "Singapore", 1.3644, 103.9915, "International", True),
        (18, "DOH", "Hamad International Airport", "Doha", "Doha", "Qatar", 25.2736, 51.6080, "International", True),
        (19, "LHR", "Heathrow Airport", "London", "England", "United Kingdom", 51.4700, -0.4543, "International", False),
        (20, "FRA", "Frankfurt Airport", "Frankfurt", "Hesse", "Germany", 50.0379, 8.5622, "International", False),
        (21, "CDG", "Charles de Gaulle Airport", "Paris", "Île-de-France", "France", 49.0097, 2.5479, "International", False),
        (22, "AMS", "Amsterdam Airport Schiphol", "Amsterdam", "North Holland", "Netherlands", 52.3105, 4.7683, "International", False),
        (23, "IST", "Istanbul Airport", "Istanbul", "Istanbul", "Turkey", 41.2753, 28.7519, "International", False),
        (24, "BKK", "Suvarnabhumi Airport", "Bangkok", "Bangkok", "Thailand", 13.6900, 100.7501, "International", False),
        (25, "KUL", "Kuala Lumpur International Airport", "Kuala Lumpur", "Selangor", "Malaysia", 2.7456, 101.7072, "International", False),
        (26, "AUH", "Zayed International Airport", "Abu Dhabi", "Abu Dhabi", "United Arab Emirates", 24.4330, 54.6511, "International", False),
        (27, "ZRH", "Zurich Airport", "Zurich", "Zurich", "Switzerland", 47.4581, 8.5555, "International", False),
        (28, "HKG", "Hong Kong International Airport", "Hong Kong", "Hong Kong", "China", 22.3080, 113.9185, "International", False),
        (29, "HND", "Tokyo Haneda Airport", "Tokyo", "Tokyo", "Japan", 35.5494, 139.7798, "International", False),
        (30, "JFK", "John F. Kennedy International Airport", "New York", "New York", "United States", 40.6413, -73.7781, "International", False)
    ]

    columns = [
        "airport_id",
        "airport_code",
        "airport_name",
        "city",
        "state",
        "country",
        "latitude",
        "longitude",
        "airport_type",
        "hub_airport"
    ]

    df = pd.DataFrame(airports, columns = columns)

    output_path = RAW_FOLDER/"dim_airport.csv"

    df.to_csv(output_path, index = False)

    print("=" * 60)
    print("AIRPORT MASTER GENERATED")
    print("=" * 60)

    print(df)

    print(f"\nTotal Airports : {len(df)}")

    print(f"\nSaved Successfully!\n{output_path}")

    return df