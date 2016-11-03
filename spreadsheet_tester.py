"""
This file makes sure that the data in the spread sheet was generated correctly

Tests spreadsheet_generator.py
"""
import json
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    root_dir = './spreadsheets/data_objects/'
    spreadsheets = [f for f in listdir(root_dir) if isfile(join(root_dir, f))]

    # make sure that each json object is valid
    for spreadsheet in spreadsheets:
        with open(root_dir + spreadsheet, 'r') as json_data:
            d = json.load(json_data)
            ref = {}
            try:
                if not type(d) == type(ref):
                    raise TypeError
            except TypeError:
                print('The generated json file was not valid')
            # add a case to make sure there are enough values and they have the correct dict keys
