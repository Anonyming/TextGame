def text(message):
    print(message)

Entytes = list()
Blocks = dict()

class Player():


    def __init__(self):

        text("Enter name (if you will play this body type iam) :")
        self.name = input()
        self.health = 100
        self.experience = 2
        self.strength = 5.2
        self.armor = 20.3
        self.x = 0
        self.y = 0
        Entytes.insert(self.name , self)

    def move(self, x, y, yn, xn):
        # yn - change y coordinate
        # xn - change x coordinate
        self.x = self.x + xn
        self.y = self.y + yn

    def attack(self, damage, target):
        if target.x == self.x + 1 or self.x - 1 and target.y == self.y + 1 or self.y - 1:
            selfdamage = damage//10
            damage = damage - target.armor
            target.health = target.health - damage
            self.health = self.health - selfdamage
        else:
            text("Target is not near")

    def build(self, amount):
        pass

    def regen(self):
        self.health = self.health + 1\

    def checklive(self):
        if self.health > 0:
            pass
        else:
            text("You die")
            self.kill
            return(False)

    def kill(self):
        Entytes.remove(self)
        if self == Entytes.iam:
            text("You lose. Restarting...")

def initPlayer():
    iam = Player()
    text("Creating your player ...")
