def mes(message):
    print(message)

Entytes = list()
Blocks = list()

class Player():


    def __init__(self):

        mes("Enter number (if you will play this body type 0) :")
        self.name = int(input())
        self.health = 100
        self.experience = 2
        self.strength = 5.2
        self.armor = 20.3
        self.x = 0
        self.y = 0
        Entytes[self.name] = self
        del(self)


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
            mes("Target is not near")

    def build(self, amount):
        pass

    def regen(self):
        self.health = self.health + 1\

    def checklive(self):
        if self.health > 0:
            pass
        else:
            mes("You die")
            self.kill
            return(False)

    def kill(self):
        if self.name == 0:
            mes("You lose. Restarting...")
        else:
            pass
        Entytes.pop(self.name)

