import json

LEVEL_MAX = 40
SPREADSHEET_PATH = './spreadsheets/data_objects/'

def calc_levels_left(char_name):
    """calculates the amount of levels a character has left to gain

    param char_name: String denoting the characters name to calc for

    rtype: int
    """
    with open(SPREADSHEET_PATH + 'starting_lvls.json', 'r') as lvls_file:
        char_lvls = json.load(lvls_file)

    char_starting_level = char_lvls[char_name]['starting_lvl']
    return LEVEL_MAX - char_starting_level


def calc_stat_gains_to_max(char_name):
    """Calculates the number of stat gains need for a character to max out all stats
    NOTE: subracts out stats gained on a class up!

    param char_name: string denoting the character name

    rtype: dict of stat gains needed to max all stats
    """
    with open(SPREADSHEET_PATH + 'character_stat_caps.json', 'r') as stat_caps_file:
        char_stat_caps = json.load(stat_caps_file)[char_name]

    with open(SPREADSHEET_PATH + 'starting_stats.json', 'r') as starting_stats_file:
        char_starting_stats = json.load(starting_stats_file)[char_name]

    with open(SPREADSHEET_PATH + 'class_change_bonuses.json', 'r') as class_change_file:
        class_change_stats = json.load(class_change_file)
        if char_name in class_change_stats:
            class_change_stats = class_change_stats[char_name]
        else:
            class_change_stats = None

    for stat_type in char_stat_caps:
        if class_change_stats is not None:
            char_stat_caps[stat_type] = char_stat_caps[stat_type] - char_starting_stats[stat_type] - class_change_stats[stat_type]
        else:
            char_stat_caps[stat_type] = char_stat_caps[stat_type] - char_starting_stats[stat_type]

    return char_stat_caps

if __name__ == '__main__':
    character = input('Which character\'s stats do you want to max? \n')
    levels_left = calc_levels_left(character)
    gains_to_max = calc_stat_gains_to_max(character)
