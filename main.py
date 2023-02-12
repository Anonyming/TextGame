class Player():


    def __init__(self):
        print("Enter name:")
        self.name = input()
        self.health = 100
        self.experience = 2
        self.strength = 5.2
        self.armor = 20.3
        self.power = 10
        self.x = 0
        self.y = 0

    def move(self, x, y, yn, xn):
        self.x = self.x + xn
        self.y = self.y + yn

    def attack(self, damage, target):
        selfharm = damage//10
        if damage - selfharm <= 0:
            print("You suicide")
            self.kill
        else:
            damage = damage - target.armor
            target.health = target.health - damage
            self.power = self.power - selfharm

    def build(self, amount):
        pass

    def regen(self):
        self.power = self.power + 1

while True:
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
        break

    else:
        print("incoorrect action")



