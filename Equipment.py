
class Equipment:
    def __init__(self, name):
        self.name = name
        if self.get_armor_type() is None:
             raise ValueError(f"Armor {name} is not supported")

    
