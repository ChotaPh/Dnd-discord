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


    shield = Shield("Shield")

    def __init__(self, char_race, char_class, char_lv):
        self.char_race = char_race
        self.char_class = char_class
        self.char_lv = char_lv
        self.abilities = self._gen_char_abilities() # _ hàm => private attribute (không gọi hàm)
        self.equip_slot = []
        self.inventory = []
        #self.proficiency = self.get_proficiency()
    def _gen_abilities_array(self):
        ability_array = []

        for _ in range(6):
            # Roll 4d6
            dice_rolls = []
            for _ in range(4):
                roll = random.randint(1, 6)
                dice_rolls.append(roll)
            sorted_dice_rolls = sorted(dice_rolls)
            dice_rolls_result = sum(sorted_dice_rolls[1:])
            ability_array.append(dice_rolls_result)
        return ability_array

    def _gen_char_abilities(self):
        abilities_array = self._gen_abilities_array()
        max_index = abilities_array.index(max(abilities_array))
        max_value = abilities_array.pop(max_index)

        abilities = {}
        match self.char_class:
            case "wizard":
                abilities["INT"] = max_value
                abilities["STR"] = abilities_array.pop(0)
                abilities["DEX"] = abilities_array.pop(0)
                abilities["CON"] = abilities_array.pop(0)
                abilities["WIS"] = abilities_array.pop(0)
                abilities["CHA"] = abilities_array.pop(0)
            case "barbarian":
                abilities["STR"] = max_value
                abilities["INT"] = abilities_array.pop(0)
                abilities["DEX"] = abilities_array.pop(0)
                abilities["CON"] = abilities_array.pop(0)
                abilities["WIS"] = abilities_array.pop(0)
                abilities["CHA"] = abilities_array.pop(0)
        return abilities

    def get_CON_modifier(self):
        return (self.abilities["CON"] - 10) / 2

    def get_STR_modifier(self):
        return (self.abilities["STR"] - 10) / 2

    def get_DEX_modifier(self):
        return (self.abilities["DEX"] - 10) / 2

    def get_INT_modifier(self):
        return (self.abilities["INT"] - 10) / 2

    def get_CHA_modifier(self):
        return (self.abilities["CHA"] - 10) / 2

    def get_WIS_modifier(self):
        return (self.abilities["WIS"] - 10) / 2

#   def get_modifier(self):
#       modifier_score = {}
#       modifier_score["STR"] = (self.abilities["STR"] - 10) / 2
#       modifier_score["DEX"] = (self.abilities["DEX"] - 10) / 2
#       modifier_score["INT"] = (self.abilities["INT"] - 10) / 2
#       modifier_score["WIS"] = (self.abilities["WIS"] - 10) / 2
#       modifier_score["CHA"] = (self.abilities["CHA"] - 10) / 2
#       return modifier_score

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


    # def cal_armor_ac(self, item: str) -> str:
    #     match item.get_armor_type():
    #         case "None":
    #             armor_ac = item.get_armor_class() + self.get_DEX_modifier()
    #         case "Light":
    #             armor_ac = item.get_ac_l_armor() + self.get_DEX_modifier()
    #         case "Medium":
    #             if self.get_DEX_modifier() <= 2:
    #                 armor_ac = item.get_ac_m_armor() + self.get_DEX_modifier()
    #             else:
    #                 armor_ac = item.get_ac_m_armor() + 2
    #         case "Heavy":
    #             armor_ac = item.get_ac_h_armor()
    #     return armor_ac


if __name__ == '__main__':
    armor = Armor("Hide")
    shield = Shield("Shield")
    def print_char_info(char_sheet: CharSheet):
        print(f"Create character sheet with race [{char_sheet.char_race}], class [{char_sheet.char_class}], level [{char_sheet.char_lv}]")
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
        print("STR: ", char_sheet.get_STR_modifier())
        print("DEX: ", char_sheet.get_DEX_modifier())
        print("CON: ", char_sheet.get_CON_modifier())
        print("WIS: ", char_sheet.get_WIS_modifier())
        print("INT: ", char_sheet.get_INT_modifier())
        print("CHA: ", char_sheet.get_CHA_modifier())
       # print("modifier ", char_sheet.get_modifier())
        print("equip: ", char_sheet.equip_slot)
        print("AC: ", char_sheet.get_ac())


    def get_file():
        with open("data.txt", "r+") as file:
            line_1 = file.readline()
            line_2 = file.readline()
            line_3 = file.readline()
        return line_1, line_2, line_3

    # tup = ("2",4, "cc")
    # first_item = tup[0] # "2"
    # second_item = tup[1]  # 4
    # third_item = tup[2]  # "cc"
    # print(f"{first_item},{second_item},{third_item}")
    #
    get_file_result = get_file()# 1 tuple
    r_race = get_file_result[0].strip()
    r_class = get_file_result[1].strip()
    r_level = get_file_result[2].strip()
    r_level = int(r_level)
    # #----
    # r_level = get_file_result[2].strip()
    # # r_level = ("human\n","wizard\n", "8")[2].strip()
    # # r_level = "8".strip()
    # # r_level = "8"
    # # r_level = 8
    # #----
    # r_level = int(r_level)
    #
    # # ASCII
    # print("get_file_result:", get_file_result)
    #
    armor = Armor("Hide")
    shield = Shield("Shield")
    char_wiz = CharSheet(r_race, r_class, r_level)
    # char_wiz.equip_item(armor.armor)
    # char_wiz.equip_item(shield.name)
    # print_char_info(char_wiz)
    char_wiz.equip_item(armor)
    char_wiz.equip_item(shield)
    print_char_info(char_wiz)


    #
    # get_file()
    # # print_char_info(get_file(CharSheet))
    # # print_char_info(get_file([Class CharSheet]))
    # # print_char_info(get_file([Class CharSheet]))


   #print_char_info(
   #    CharSheet(
   #        "human",
   #        "wizard",
   #        8
   #    )
   #)

    # Create class armor
    # Attribute
    #   - armor name
    #   - armor class
    #   - method for calculate AC
    #   - Load from file

    '''
    1. equip armor and shield
    2. print armor ac with Dex modifier bonus
    3. print armor ac with equipped shield
    4. print armor ac without equipped shield
    '''
  #  CharSheet.get_equiment(Armor)

#   armor_char = Armor("Plate")
#   shield = Shield("Shield")
#   equipped = []
#   def get_equiment(armor_char,shield):
#       equipped.append(armor_char.armor)
#       equipped.append(shield.shield)

#       return equipped


#   print("Armor equipped: ", get_equiment(armor_char,shield))


#   def cal_armor_ac():
#       match armor_char.get_armor_type():
#           case "None":
#               armor_ac = armor_char.get_armor_class() + char_wiz.get_DEX_modifier()
#           case "Light":
#               armor_ac = armor_char.get_ac_l_armor() + char_wiz.get_DEX_modifier()
#           case "Medium":
#               if char_wiz.get_DEX_modifier() <= 2:
#                   armor_ac = armor_char.get_ac_m_armor() + char_wiz.get_DEX_modifier()
#               else:
#                   armor_ac = armor_char.get_ac_m_armor() + 2
#           case "Heavy":
#               armor_ac = armor_char.get_ac_h_armor()
#       return armor_ac

#   def cal_equipped_ac():
#       if equipped[1] == "Shield":
#           equipped_ac = cal_armor_ac() + shield.get_shield()
#       elif equipped[1] == "None":
#           equipped_ac = cal_armor_ac()
#       return equipped_ac

#   print(f"Armor type: {armor_char.get_armor_type()} - Armor: {armor_char.armor}")
#   print("Armor AC: ",cal_equipped_ac())




