from animal import Animal

class Repile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amnioic_eggs = None


    def seek_heat(self):
        print("its chilly outside, wheres the sun?")

    def hunt(self):
        print("wait, wait,wait")

    def use_venom(self):
        print("if you have it use it")

    def attract_trough_scent(self):
        print("time to spray perfume")

jeremy_the_reptile = Repile()
jeremy_the_reptile.breathe()
jeremy_the_reptile.hunt()
jeremy_the_reptile.eat()
#encap