from Equipment import Equipment

'''
    1. create shield ac
'''


class Shield(Equipment):
    def __init__(self, shield):
        self.name = shield
    def get_armor_class(self):
        return 2
