import json
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    root_dir = './spreadsheets/spreadsheet_sources/'
    filenames = [f for f in listdir(root_dir) if isfile(join(root_dir, f))]

    for raw_data_file in filenames:
        name = {}
        filename = str(root_dir + raw_data_file)
        with open(filename, 'r') as inFile:
            for line in inFile:
                s = line.split()
                name[s[0]] = {}
                name[s[0]]['HP'] = s[1]
                name[s[0]]['Str'] = s[2]
                name[s[0]]['Mag'] = s[3]
                name[s[0]]['Skl'] = s[4]
                name[s[0]]['Spd'] = s[5]
                name[s[0]]['Luck'] = s[6]
                name[s[0]]['Def'] = s[7]
                name[s[0]]['Res'] = s[8]

            stats_file = './spreadsheets/data_objects/' + raw_data_file
            with open(stats_file, 'w') as dump_file:
                json.dump(name, dump_file)
