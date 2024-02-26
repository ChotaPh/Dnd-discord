from CharSheet import CharSheet
'''import date time CLI creator library argparse'''
import argparse
'''import date time library'''
import datetime
from Equipment import Equipment
import random
from Armor import Armor
from Shield import Shield


'''
1. Create character CLI command
2. when enter command create a Txt to store info
3. input in name, class and race to get info from CharSheet.py
4. print out the character sheet on CMD and Txt file
'''

'''create instance of class ArgumentParser'''
parser = argparse.ArgumentParser()

'''Call add_argument function'''
'''create command cr-char to create char'''
parser.add_argument('create',choices=['cr-char'],  help='create your dnd character')

'''parse or change the argument script to computer language'''
args = parser.parse_args()

try:
    '''condition'''
    while args.create == 'cr-char':
        ''' create character file at current time'''
        character = datetime.datetime.now().strftime("Character %Y-%m-%d_%H-%M-%S") + ".txt"
        '''w+ create new file if it not yet exist'''
        with open(character, "w+") as file:
            file.write(input("Name: ") + "\n")
            file.write(input("Race: ") + "\n")
            file.write(input("Class: ") + "\n")
            file.write(input("Level: ") + "\n")

        '''create function read from character file'''


        def get_file():
            with open(character, "r+") as file:
                line_1 = file.readline()
                line_2 = file.readline()
                line_3 = file.readline()
                line_4 = file.readline()
                return line_1, line_2, line_3, line_4


        get_file_result = get_file()
        r_name = get_file_result[0].strip()
        r_race = get_file_result[1].strip()
        r_class = get_file_result[2].strip()
        r_level = get_file_result[3].strip()
        r_level = int(r_level)


        def print_char_info(char_sheet: CharSheet):
            print(
                f"Create character sheet with race [{char_sheet.char_race}], class [{char_sheet.char_class}], level [{char_sheet.char_lv}]")
            print("proficiency: ", char_sheet.get_proficiency())

            print("Abilities: ")
            print("STR: ", char_sheet.abilities["STR"])
            print("DEX: ", char_sheet.abilities["DEX"])
            print("CON: ", char_sheet.abilities["CON"])
            print("WIS: ", char_sheet.abilities["WIS"])
            print("INT: ", char_sheet.abilities["INT"])
            print("CHA: ", char_sheet.abilities["CHA"])

            print("HP: ", char_sheet.get_max_hp())

            print("Modifier: ")
            print("STR: ", round(char_sheet.get_STR_modifier()))
            print("DEX: ", round(char_sheet.get_DEX_modifier()))
            print("CON: ", round(char_sheet.get_CON_modifier()))
            print("WIS: ", round(char_sheet.get_WIS_modifier()))
            print("INT: ", round(char_sheet.get_INT_modifier()))
            print("CHA: ", round(char_sheet.get_CHA_modifier()))
            # print("modifier ", char_sheet.get_modifier())
            equipment_name = []
            for equipment in char_sheet.equip_slot:
                equipment_name.append(equipment.name)
            print(equipment_name)


        armor = Armor("Plate")
        shield = Shield("Shield")
        char_wiz = CharSheet(r_race, r_class, r_level)
        char_wiz.equip_item(armor)
        char_wiz.equip_item(shield)
        char_wiz.unequip_item(armor)
        char_wiz.equip_item(armor)
        print_char_info(char_wiz)
except KeyboardInterrupt:
    print("\n welcome traveler")


