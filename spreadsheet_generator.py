import json
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    root_dir = './spreadsheets/spreadsheet_sources/'
    filenames = [f for f in listdir(root_dir) if isfile(join(root_dir, f))]

    for raw_data_file in filenames:
        try:
            name = {}
            filename = str(root_dir + raw_data_file)
            with open(filename, 'r') as inFile:
                for line in inFile: # this line is probably inefficient cuz of the amount of checks it takes, but whatever
                    if raw_data_file == 'BExp_adjusted_growth_rates.txt':
                        s = line.split()
                        name[s[0]] = {}
                        name[s[0]]['1'] = float(s[1])
                        name[s[0]]['2'] = float(s[2])
                        name[s[0]]['3'] = float(s[3])
                        name[s[0]]['4'] = float(s[4])
                        name[s[0]]['5'] = float(s[5])
                        name[s[0]]['10'] = float(s[6])
                    elif raw_data_file == 'character_growth_rates.txt' or raw_data_file == 'character_stat_caps':
                        s = line.split()
                        name[s[0]] = {}
                        name[s[0]]['HP'] = int(s[1])
                        name[s[0]]['Str'] = int(s[2])
                        name[s[0]]['Mag'] = int(s[3])
                        name[s[0]]['Skl'] = int(s[4])
                        name[s[0]]['Spd'] = int(s[5])
                        name[s[0]]['Def'] = int(s[6])
                        name[s[0]]['Res'] = int(s[7])
                        name[s[0]]['Luck'] = int(s[8])
                    else:
                        s = line.split()
                        name[s[0]] = {}
                        name[s[0]]['HP'] = int(s[1])
                        name[s[0]]['Str'] = int(s[2])
                        name[s[0]]['Mag'] = int(s[3])
                        name[s[0]]['Skl'] = int(s[4])
                        name[s[0]]['Spd'] = int(s[5])
                        name[s[0]]['Luck'] = int(s[6])
                        name[s[0]]['Def'] = int(s[7])
                        name[s[0]]['Res'] = int(s[8])
        except ValueError:
            print('The value Error occured in: ' + raw_data_file)
            print('On line ' + line)

        stats_file = './spreadsheets/data_objects/' + \
            raw_data_file[0:-5] + '.json'
        with open(stats_file, 'w') as dump_file:
            json.dump(name, dump_file)
