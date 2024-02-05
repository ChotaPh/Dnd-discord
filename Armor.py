from Equipment import Equipment

"""
Class vs Logic vs Argument ?

Class
    => compose of functions/logic
    => Instance
        => class with data
Logic
    if,else, for loop,....

Argument
    input data of the function
"""


# class CharSheet:
#     def __init__(self, race, lv, armor, boot, hat):
#         #
#         pass
#
#     def apply_debuff(self, debuff):
#         self.debuffs.append(debuff)
#
#     def get_ac(self):
#         if "bar" and (self.armor == None or self.armor.get_armor_type() == "No protection"):
#             # Logic
#             if "hex" in self.debuffs:
#                 ac = ac - 1
#             # Logic
#             return ac
# # Bar
# CharSheet("bar", 1, None, "boot", "hat")
#
# ranger_armor = Armor("Hide")
# CharSheet("Ranger", 1, ranger_armor, "boot", "hat")

class Armor(Equipment):
    """
        armor: the metal coverings formerly worn by soldiers or warriors to protect the body in battle.
        1. phân nhóm armor light, medium, heavy or none
        2. gắn chỉ số ac phù hợp trong cho từng loại armor trong light medium và heavy
        3. đọc text in ra ac của armor (tạm thời)
        ---
        Raise error when input not supported armor_type, armor
    """
    simple_armor_class = {"Robe"}
    light_armor_class = {"Padded", "Leather", "Studded"}
    medium_armor_class = {"Hide", "Chain Shirt", "Scale Mail", "Breast Plate", "Half Plate"}
    heavy_armor_class = {"Ring Mail", "Chain Mail", "Splint", "Plate"}
    shield_armor_class = {"Shield"}

  # def __init__(self, armor):
  #     self.name = armor
  #     if self.get_armor_type() is None:
  #         raise ValueError(f"Armor {armor} is not supported")

    def get_armor_type(self):
        if self.name in Armor.simple_armor_class:
            return "Simple"
        if self.name in Armor.light_armor_class:
            return "Light"
        if self.name in Armor.medium_armor_class:
            return "Medium"
        if self.name in Armor.heavy_armor_class:
            return "Heavy"

    def get_armor_class(self):
        armor_ac = None
        match self.get_armor_type():
            case "Simple":
                armor_ac = 10
            case "Light":
                armor_ac = self.get_ac_l_armor()
            case "Medium":
                armor_ac = self.get_ac_m_armor()
            case "Heavy":
                armor_ac = self.get_ac_h_armor()
        return armor_ac

    def get_ac_l_armor(self):
        armor_ac = 11
        match self.name:
            case "Padded":
                armor_ac = armor_ac
            case "Leather":
                armor_ac = armor_ac
            case "Studded":
                armor_ac = armor_ac + 1
        return armor_ac

    def get_ac_m_armor(self):
        armor_ac = 12
        match self.name:
            case "Hide":
                armor_ac = armor_ac
            case "Chain Shirt":
                armor_ac = armor_ac + 1
            case "Scale Mail":
                armor_ac = armor_ac + 2
            case "Breast Plate":
                armor_ac = armor_ac + 2
            case "Half Plate":
                armor_ac = armor_ac + 3
        return armor_ac

    def get_ac_h_armor(self):
        armor_ac = 14
        match self.name:
            case "Ring Mail":
                armor_ac = armor_ac
            case "Chain Mail":
                armor_ac = armor_ac + 2
            case "Splint":
                armor_ac = armor_ac + 3
            case "Plate":
                armor_ac = armor_ac + 4
        return armor_ac


if __name__ == '__main__':
    def print_char_info(armor):
        print(f"Create character sheet with armor type [{armor.get_armor_type()}], armor[{armor.name}]")
        print("Armor's AC: ", armor.get_armor_class())


    armor_char = Armor("Breast Plate")
    print_char_info(armor_char)
# hide_armor = Armor("Hide")
# print("Armor type: ", hide_armor.get_armor_type())
# print("Armor's AC: ", hide_armor.get_armor_class())

#
# l_armor = {"Padded","Leather","Studded"}
# if ArmorClass.armor_type == l_armor:
#     if ArmorClass.armor == {"Padded", "Leather", "Studded"}:
#         True
#     else:
#         raise ("armor does not belong in light armor")
#
# armor_char = ArmorClass("human","wizard","1","Light","Leather")
#
#
# #print_char_info(armor_char)
#
