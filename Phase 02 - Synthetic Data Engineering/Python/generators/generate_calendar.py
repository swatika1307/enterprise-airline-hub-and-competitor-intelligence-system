'''
Generate Calendar Dimension
Enterprise Airline Hub & Competitor Intelligence System

Date Started - 19.07.2026
Last Modified - 20.07.2026
'''

import pandas as pd

from config.paths import RAW_FOLDER
from config.config import PROJECT_YEAR

def generate_calendar():
    start_date = f"{PROJECT_YEAR}-01-01"
    end_date = f"{PROJECT_YEAR + 2}-12-31"
    dates = pd.date_range(
        start = start_date,
        end = end_date,
        freq = "D"
    )
    calendar_records = []
    financial_quarter_map = {
        4 : "Q1",
        5 : "Q1",
        6 : "Q1",
        7 : "Q2",
        8 : "Q2",
        9 : "Q2",
        10 : "Q3",
        11 : "Q3",
        12 : "Q3",
        1 : "Q4",
        2 : "Q4",
        3 : "Q4"
    }
    season_map = {
        12 : "Winter",
        1 : "Winter",
        2 : "Winter",
        3 : "Summer",
        4 : "Summer",
        5 : "Summer",
        6 : "Monsoon",
        7 : "Monsoon",
        8 : "Monsoon",
        9 : "Monsoon",
        10 : "Post-Monsoon",
        11 : "Post-Monsoon"
    }
    peak_months = [4, 5, 6, 10, 11, 12]
    for date in dates:
        month = date.month
        financial_year = (
            f"FY{date.year}-{str(date.year + 1)[-2:]}"
            if month >= 4
            else f"FY{date.year - 1}-{str(date.year)[-2:]}"
        )
        calendar_records.append({
            # Identity
            "date_id" : int(date.strftime("%Y%m%d")),
            "full_date" : date.date(),
            # Calendar
            "day" : date.day,
            "month" : month,
            "month_name" : date.strftime("%B"),
            "month_short" : date.strftime("%b"),
            "quarter" : f"Q{date.quarter}",
            "year" : date.year,
            # Weekly
            "day_of_week" : date.dayofweek + 1,
            "day_name" : date.strftime("%A"),
            "week_of_year" : int(date.isocalendar().week),
            "day_of_year" : date.dayofyear,
            "week_start_date" : (
                date - pd.Timedelta(days = date.dayofweek)
            ).date(),
            "week_end_date" : (
                date + pd.Timedelta(days = 6 - date.dayofweek)
            ).date(),
            # Reporting
            "year_month" : date.strftime("%Y-%m"),
            "month_year" : date.strftime("%b-%Y"),
            # Calendar Flags
            "is_weekend" : date.dayofweek >= 5,
            "weekday_type" : (
                "Weekend"
                if date.dayofweek >= 5
                else "Weekday"
            ),
            "is_month_start" : date.is_month_start,
            "is_month_end" : date.is_month_end,
            "is_quarter_start" : date.is_quarter_start,
            "is_quarter_end" : date.is_quarter_end,
            "is_year_start" : date.is_year_start,
            "is_year_end" : date.is_year_end,
            "is_leap_year" : date.is_leap_year,
            # Financial Calendar
            "financial_year" : financial_year,
            "financial_quarter" : financial_quarter_map[month],
            # Airline Analytics
            "season" : season_map[month],
            "travel_season" : (
                "Peak"
                if month in peak_months
                else "Off-Peak"
            ),
            "is_public_holiday" : False,
            "is_long_weekend" : False
        })

    df = pd. DataFrame(calendar_records)

    output_path = RAW_FOLDER/"dim_calendar.csv"

    df.to_csv(output_path, index = False)

    print("=" * 60)
    print("CALENDAR DIMENSION GENERATED")
    print("=" * 60)

    print(df.head())

    print(f"\nTotal Dates : {len(df)}")

    print(f"\nSaved Successfully!\n{output_path}")

    return df