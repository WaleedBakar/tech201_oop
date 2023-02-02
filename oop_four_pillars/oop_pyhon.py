from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False


    def digest_larg_prey(self):
        print("ok let me get the stretchy pants")

    def constrict(self):
        print("squeeeeeeeze")

    def shed_skin(self):
        print("im growing out of this now ")

peter  = Python()
peter.breathe()
peter.use_tongue_to_smell()
peter.hunt()
peter.shed_skin()