""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

def import_table():
    data_table = data_manager.read_table_from_file(DATAFILE, ";")
    return data_table

def export_table(table):
     data_manager.write_table_to_file(DATAFILE, table, ";")