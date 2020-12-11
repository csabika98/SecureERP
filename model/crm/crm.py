""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crmsubscribed.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def import_table():
    data_table = data_manager.read_table_from_file(DATAFILE, ";")
    return data_table

def export_table(table):
     data_manager.write_table_to_file(DATAFILE, table, ";")