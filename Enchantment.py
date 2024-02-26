from Equipment import Equipment
from Armor import Armor
'''
1. create enchantment number
2. enchantment number is in front of equpiment name
3. if equipment have
'''
class Enchantment():
    def __init__(self, en_num: int):
        self.enchant = en_num

    def get_entchanment(self):
        armor_class = 10
        for equipment in self.e_slot:
            if hasattr(equipment, 'get_armor_class'):
                armor_class = equipment.get_armor_class() + self.enchant
                return armor_class


