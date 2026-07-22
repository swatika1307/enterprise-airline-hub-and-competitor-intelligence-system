'''
Project Paths

Date Started - 15.07.2026
Last Modified - 15.07.2026
'''

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_FOLDER = PROJECT_ROOT / "data"

RAW_FOLDER = DATA_FOLDER / "raw"

PROCESSED_FOLDER = DATA_FOLDER / "processed"

EXPORT_FOLDER = DATA_FOLDER / "exports"

OUTPUT_FOLDER = PROJECT_ROOT / "output"

RAW_FOLDER.mkdir(parents = True, exist_ok = True)
PROCESSED_FOLDER.mkdir(parents = True, exist_ok = True)
EXPORT_FOLDER.mkdir(parents = True, exist_ok = True)
OUTPUT_FOLDER.mkdir(parents = True, exist_ok = True)