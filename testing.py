from Equipment import Equipment
import random
from Armor import Armor
from Shield import Shield


class CharSheet:
    '''
        1. Generate ability score
            For each of abi array
                Generate 4 d6
                Remove lowest
                sum the rest -> result for abi
            Get highest of abi array, set to main stats for class
            randomize for the rest of stats
        2. Get modifiers
        3. Generate HP
        4. Get level
        5. get proficiency
    '''



    '''initialize instance if it in def ..(self) it is none define type '''
    def __init__(self, char_race, char_class, char_lv):
        self.char_race = char_race
        self.char_class = char_class
        self.char_lv = char_lv
        '''each ability name is key in ab dictionary, and their value initiate at 0'''
        self.abilities = {"STR":0,"DEX":0,"CON":0,"INT":0,"WIS":0,"CHA":0} # _ hàm => private attribute (không gọi hàm)
        self.abilities_arr = self._gen_abilities_array()
        self.equip_slot = []
        self.inventory = []
        #self.proficiency = self.get_proficiency()
    def _gen_abilities_array(self):
        self.array = []

        for _ in range(6):
            # Roll 4d6
            dice_rolls = []
            for _ in range(4):
                roll = random.randint(1, 6)
                dice_rolls.append(roll)
            sorted_dice_rolls = sorted(dice_rolls)
            dice_rolls_result = sum(sorted_dice_rolls[1:])
            self.array.append(dice_rolls_result)
        return self.array
    '''function to store one ablity array prevent dublicate'''
    def _gen_char_abilities(self):
       abilities_array = self._gen_abilities_array()
 #     max_index = abilities_array.index(max(abilities_array))
 #     max_value = abilities_array.pop(max_index)
 #     print(abilities_array)
 #     '''each ability name is key in ab dictionary, and their value initiate at 0'''






    def get_CON_modifier(self):

            return (self.abilities["CON"] - 10) / 2

    def get_WIS_modifier(self):
        try:
            return (self.abilities["WIS"] - 10) / 2
        except:
            return 0

    def get_STR_modifier(self):
        try:
            return (self.abilities["STR"] - 10) / 2
        except:
            return 0

    def get_DEX_modifier(self):
        try:
            return (self.abilities["DEX"] - 10) / 2
        except:
            return 0

    def get_INT_modifier(self):
        try:
            return (self.abilities["INT"] - 10) / 2
        except:
            return 0
    def get_CHA_modifier(self):
        try:
            return (self.abilities["CHA"] - 10) / 2
        except:
            return 0




    def get_max_hp(self):
        match self.char_class:
            case "wizard":
                return self.get_CON_modifier() + 8
            case "barbarian":
                return self.get_CON_modifier() + 12
            case _:
                raise Exception(f"Get HP for class {self.char_class} not supported.")

    def get_proficiency(self):
        '''
        level from 1 to 4 proficiency = 2
        level from 5 to 8 proficiency = 3
        level from 9 to 12 proficiency = 4
        level from 13 to 16 proficiency = 5
        level from 17 to 20 proficiency = 6
        '''
        level = self.char_lv
        if level <= 4:
            return 2
        elif 5 <= level <= 8:
            return 3
        elif 9 <= level <= 12:
            return 4
        elif 13 <= level <= 16:
            return 5
        elif 17 <= level <= 20:
            return 6

    def equip_item(self, item: Equipment):
        self.equip_slot.append(item)

    def unequip_item(self, item: Equipment):
        self.equip_slot.remove(item)

    # base ac of naked, simple cloth = 10
    def get_ac(self):
        armor_class = self._get_armor_ac()
        for equipment in self.equip_slot:
            if hasattr(equipment, 'get_armor_class') and not isinstance(equipment, Armor):
                armor_class += equipment.get_armor_class()
        return armor_class

    def _get_armor_ac(self):
        armor_class = 10
        for equipment in self.equip_slot:
            if isinstance(equipment, Armor):
                armor_class = equipment.get_armor_class()
                match equipment.get_armor_type():
                    case "Simple":
                        armor_class += self.get_DEX_modifier()
                    case "Light":
                        armor_class += self.get_DEX_modifier()
                    case "Medium":
                        armor_class += min(self.get_DEX_modifier(), 2)
        return armor_class



if __name__ == '__main__':
    armor = Armor("Plate")
    shield = Shield("Shield")
    def print_char_info(char_sheet: CharSheet):
        print(f"Create character sheet with race [{char_sheet.char_race}], class [{char_sheet.char_class}], level [{char_sheet.char_lv}]")
        print("proficiency: ", char_sheet.get_proficiency())
        dice_result = char_sheet.abilities_arr
        print(dice_result)

        '''repeat input until it in dice_result list'''
        while True:
          STR = input("STR: ")
          char_sheet.abilities['STR'] = int(STR)
          int_STR = int(STR)
          '''if input not in list mean you cheat'''
          if int_STR not in dice_result:
              print("Do not cheat")
          else:
              for st in range (0, 5):
                  if int_STR == dice_result[st]:
                      '''remove the number of list > prevent player use number again'''
                      dice_result.remove(int_STR)
                      '''break for loop when condition met > prevent random index over range'''
                      break
              break

        while True:
          DEX = input("DEX: ")
          char_sheet.abilities['DEX'] = int(DEX)
          int_DEX = int(DEX)
          if int_DEX not in dice_result:
              print("Do not cheat")
          else:
              for dex in range (0, 4):
                  if int_DEX == dice_result[dex]:
                      dice_result.remove(int_DEX)
                      break
              break

        while True:
          CON = input("CON: ")
          char_sheet.abilities['CON'] = int(CON)
          int_CON = int(CON)
          if int_CON not in dice_result:
              print("Do not cheat")
          else:
              for con in range (0, 3):
                  if int_CON == dice_result[con]:
                      dice_result.remove(int_CON)
                      break
              break

        while True:
            INT = input("INT: ")
            char_sheet.abilities['INT'] = int(INT)
            int_INT = int(INT)
            if int_INT not in dice_result:
                print("Do not cheat")
            else:
                for ints in range(0, 2):
                    if int_INT == dice_result[ints]:
                        dice_result.remove(int_INT)
                        break
                break

        while True:
            WIS = input("WIS: ")
            char_sheet.abilities['WIS'] = int(WIS)
            int_WIS = int(WIS)
            if int_WIS not in dice_result:
                print("Do not cheat")
            else:
                for wis in range(1):
                    if int_WIS == dice_result[wis]:
                        dice_result.remove(int_WIS)
                        break
                break

        while True:
            CHA = input("CHA: ")
            char_sheet.abilities['CHA'] = int(CHA)
            int_CHA = int(CHA)
            if int_CHA not in dice_result:
                print("Do not cheat")
            else:
                for cha in range(0):
                    if int_CHA == dice_result[cha]:
                        dice_result.remove(int_CHA)
                break




        print(char_sheet.abilities)




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

     #  print("equip: ", char_sheet.equip_slot[0].name)
     #  print("equip: ", char_sheet.equip_slot[1].name)
        print("AC: ", round(char_sheet.get_ac()))




    char_wiz = CharSheet("elf","wizard", 3)

    char_wiz.equip_item(armor)
    char_wiz.equip_item(shield)
    char_wiz.unequip_item(armor)
    char_wiz.equip_item(armor)
    print_char_info(char_wiz)
