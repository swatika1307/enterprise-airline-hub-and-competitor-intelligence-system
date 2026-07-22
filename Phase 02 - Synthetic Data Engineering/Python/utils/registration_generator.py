'''
Aircraft Registration Number Generator
Enterprise Airline Hub & Competitor Intelligence System

Date Started - 16.07.2026
Last Modified - 16.07.2026
'''

def generate_registration(prefix : str, number : int) -> str:
    return f"{prefix}-{number:03d}"