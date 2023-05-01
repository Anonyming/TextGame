Entytes = list()  # some DBs
Blocks = list()

class Block():  # the block class
    def __init__(self, x, y):
        x = x
        y = y
        Blocks.append(self)

    def __del__(self):
        print(f'Block at x:{self.x} y:{self.y} destroyed')

class Player():  # the player class


    def __init__(self):

        print("enter name:")
        self.name = input()
        self.health = 100
        self.experience = 2
        self.strength = 5.2
        self.armor = 20.3
        self.x = 0
        self.y = 0
        Entytes.append(self)  # add to DB


    def move(self, x, y, yn, xn):  # move to some coordinates
        # yn - change y coordinate
        # xn - change x coordinate
        self.x = self.x + xn
        self.y = self.y + yn

    def attack(self, damage, target):  ## attack some entyty
        if target.x == self.x + 1 or self.x - 1 and target.y == self.y + 1 or self.y - 1:  # attacker is near
            selfdamage = damage//10  # weary
            damage = damage - target.armor
            target.health = target.health - damage
            self.health = self.health - selfdamage
        else:  # attacker is not near
            print("Target is not near")

    def regen(self):  # regen self
        self.health = self.health + 1\

    def checklive(self):  # chck for live or die
        if self.health > 0:
            pass
        else:
            print(f'{self.name} die')
            self.kill
            return(False)

    def kill(self):  # die
        if self.name == 0:
            print("You lose. Restarting...")
        else:
            pass
        Entytes.pop(self)
        self.__del__()

    def __del__(self):
        print(f'{self.name} die')

def initPlayer():  # init the player
    print("Creating your player ...")
    iam = Player()
