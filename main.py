Entytes = list()
Blocks = list()
class Block():
    y = 0
    x = 0
    def __init__(self):
        Blocks.insert(len(Blocks) + 1 , self )

    def delete(self):
        Blocks.remove(self)

class Player():


    def __init__(self):

        print("Enter name (if you will play this body type iam) :")
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
            print("Target is not near")

    def build(self, amount):
        pass

    def regen(self):
        self.health = self.health + 1\

    def checklive(self):
        if self.health > 0:
            pass
        else:
            print("You die")
            self.kill
            return(False)

    def kill(self):
        Entytes.remove(self)
        if self == iam:
            initPlayer()

def initPlayer:
    iam = Player()
    print("Creating your player ...")
    main()

def main:

    while True:

        i = 0

        while i <= len(Entytes):
            Entytes(i).cheklive

        action = input()

        if action == "join":
            iam = Player()

        elif action == "add entyty":
            added = Player()

        elif action == "attack":
            print("Enter target:")
            target = input()
            print("Enter power of attack:")
            damage = int(input())
            iam.attack(damage, target)

        elif action == "move":
            print("Enter distance x:")
            xn = int(input())
            print("also y:")
            yn = int(input())
            iam.move(iam.x, iam.y, xn, yn)

        elif action == "exit":
            quit(0)

        elif action == "set block":
            print("Enter location")
            print("x:")
            blockx = int(input())
            print("y:")
            blocky = int(input())
            if iam.x + 1 or - 1 == blockx and iam.y + 1 or - 1 == blocky
                new = Block()
                Blocks(len(Blocks)).y = blocky
                Blocks(len(Blocks)).x = blockx
            elif iam.x == blockx and iam.y == blocky:
                print("You can't create block at youself")
                main()
            else:
                print("It not near")
                main()

        else:
            print("incoorrect action")
            main()