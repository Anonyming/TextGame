Entytes = list()
class Player():


    def __init__(self):

        print("Enter name:")
        self.name = input()
        self.health = 100
        self.experience = 2
        self.strength = 5.2
        self.armor = 20.3
        self.x = 0
        self.y = 0
        Entytes.insert(len(Entytes) , self)

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
            print("You suicided")
            self.kill

Player.iam
Print("Creating your player ...")

while True:

 i = 0
    while i <= len(Entytes):
        Entytes(i).cheklive

    action = input()

    if action == "join":
        iam = Player()

    elif action == "add player":
        added = Player()

    elif action == "attack":
        print("Enter target:")
        target = input()
        print("Enter power of attack:")
        damage = input()
        iam.attack(damage, target)

    elif action == "move":
        print("Enter distance x:")
        xn = input()
        print("also y:")
        yn = input()
        iam.move(iam.x, iam.y, xn, yn)

    elif action == "exit":
        quit(0)

    else:
        print("incoorrect action")