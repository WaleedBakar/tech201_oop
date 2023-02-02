from  reptile import Repile

class Snake(Repile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None
        self.limbs = False


    def use_tongue_to_smell(self):
        print("do i say it smells or tastes nicee?")

sidney = Snake()
sidney.seek_heat()
# poly