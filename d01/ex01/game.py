class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.name = first_name
class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Comming"
    
    def print_house_words(self):
        return (self.house_words)
    
    def die(self):
        self.is_alive = False