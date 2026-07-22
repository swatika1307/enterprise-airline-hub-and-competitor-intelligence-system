'''
Main Entry Point

Date Started - 15.07.2026
Last Modified - 20.07.2026
'''

# Step 2.1 - Project Structure and Configuration Setup
# initial check - project initialization
from config.config import PROJECT_NAME
from config.config import PROJECT_YEAR

# Step 2.2 - Generate Airline Master Dataset
# generate_airlines - as the generate_airlines.py was giving config module not found error
from generators.generate_airlines import generate_airlines

# Step 2.3 - Generate Airport Master Dataset
from generators.generate_airports import generate_airports

# Step 2.4 - Generate Aircraft Master Dataset
# 1st file - util.registration_generator.py
# 2nd file - generators.generate_aircraft.py
from generators.generate_aircraft import generate_aircraft

# Step 2.5 - Route Network Generation
# 1st file - Create a reusable distance utility - utils.distance_calculator.py
# 2nd file - update constants.py
# 3rd file - airport lookup - utils.airport_lookup.py
# 4th file - generate_routes.py
# 5th file - generate_airline_routes.py
from generators.generate_routes import generate_routes
from generators.generate_airline_routes import generate_airline_routes

# Step 2.6 - Calendar Generation
# 1st file - generate_calendar.py
from generators.generate_calendar import generate_calendar

# -----------------
# DEVELOPMENT MODE
# -----------------
RUN_ALL = False

RUN_AIRLINES = False
RUN_AIRPORTS = False
RUN_AIRCRAFT = False
RUN_ROUTES = False
RUN_BRIDGE = False
RUN_CALENDAR = True

# --------------
# MAIN FUNCTION 
# --------------
def main():
    # Step 2.1 - Project Structure and Configuration Setup
    # initial check - project initialization
    print("=" * 60)
    print(PROJECT_NAME)
    print("=" * 60)
    print(f"Simulation Year : {PROJECT_YEAR}")
    print("\nProject Initialized Successfully.")

    # Step 2.2 - Generate Airline Master Dataset
    # generate_airlines - as the generate_airlines.py was giving config module not found error
    if RUN_ALL or RUN_AIRLINES:
        print("\nGenerating Airline Master...\n")
        generate_airlines()
        print("\nProcess Completed Successfully.")

    # Step 2.3 - Generate Airport Master Dataset
    if RUN_ALL or RUN_AIRPORTS:
        print("\nGenerating Airport Master...\n")
        generate_airports()
        print("\nProcess Completed Successfully.")

    # Step 2.4 - Generate Aircraft Master Dataset
    # 1st file - util.registration_generator.py
    # 2nd file - generators.generate_aircraft.py
    if RUN_ALL or RUN_AIRCRAFT:
        print("\nGenerating Aircraft Fleet...\n")
        generate_aircraft()
        print("\nProcess Completed Successfully.")

    # Step 2.5 - Route Network Generation
    # 1st file - Create a reusable distance utility - utils.distance_calculator.py
    # 2nd file - update constants.py
    # 3rd file - airport lookup - utils.airport_lookup.py
    # 4th file - generate_routes.py
    if RUN_ALL or RUN_ROUTES:
        print("\nGenerating Route Master...\n")
        generate_routes()
        print("\nProcess Completed Successfully.")
    # 5th file - generate_airline_routes.py
    if RUN_ALL or RUN_BRIDGE:
        print("\nGenerating Bridge Route Master...\n")
        generate_airline_routes()
        print("\nProcess Completed Successfully.")

    # Step 2.6 - Calendar Generation
    # 1st file - generate_calendar.py
    if RUN_ALL or RUN_CALENDAR:
        print("\nGenerating Calendar Dimension...\n")
        generate_calendar()
        print("\nProcess Completed Successfully.")

if __name__ == "__main__":
    main()