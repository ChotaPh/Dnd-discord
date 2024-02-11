from Equipment import Equipment

'''
    1. create shield ac
'''


class Shield(Equipment):
    shield = {"Shield"}

    #def __init__(self):
        #self.name = shield

    def get_armor_type(self):
        if self.name in Shield.shield:
            return "Shield"


    def get_armor_class(self):
        return 2
